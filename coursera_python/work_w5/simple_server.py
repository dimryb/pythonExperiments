# реализация сервера для тестирования метода get по заданию - Клиент для отправки метрик
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

# переменная response хранит строку возвращаемую сервером, если вам для
# тестирования клиента необходим другой ответ, измените ее
response = b'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
bad_response1 = b'ok\npalm.cpu 10,5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
bad_response2 = b'ok\npalm.cpu 10,5 1501864247 d\neardrum.cpu 15.3 1501864259\n\n'
bad_response3 = b'ok\npalm.cpu 10 \neardrum.cpu 15.3 1501864259\n\n'
bad_response4 = b'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'

base = {"palm.cpu": [(1501864247, 10.5), (1150864248, 0.5)], "eardrum.cpu": [(1501864259, 15.3)]}


def get_all_response():
    return get_metric_response()


def get_metric_response(request_key=None):
    resp = "ok\n"
    for key in base:
        if request_key:
            if key != request_key:
                continue
        metric_pairs_list = base[key]
        print(metric_pairs_list)

        for metric_pair in metric_pairs_list:
            print(metric_pair)
            resp += key + " "
            resp += str(metric_pair[1]) + " " + str(metric_pair[0])
            resp += "\n"
            pass

    resp += "\n"
    return resp.encode()


def put_metric_response(request):
    pass


# print (get_all_response())
# print (get_metric_response("eardrum.cpu"))

sock = socket.socket()
sock.bind(('127.0.0.1', 8889))
sock.listen(1)
conn, addr = sock.accept()

print('Соединение установлено:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    request = data.decode('utf-8')
    print(f'Получен запрос: {ascii(request)}')

    split_req = request.split()
    print(split_req)
    if split_req[0] == 'get' and len(split_req) == 2:
        if split_req[1] == "*":
            print("split_req[1] == '*'")
            response = get_all_response()
        else:
            response = get_metric_response(split_req[1])
    elif split_req[0] == 'put' and len(split_req) == 4:
        response = b"ok\n\n"
    else:
        response = b"error\nwrong command\n\n"

    # time.sleep(1)

    # response = bad_response3

    print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
    conn.send(response)

conn.close()
