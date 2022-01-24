import bisect
import socket
import time


class ClientError(Exception):
    """класс исключений клиента"""

    def __init__(self, text, *args):
        print("Client error: ", text, args)



class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError("Cannot create connection", err)

    def _read(self):

        data = b""

        while not data.endswith(b"\n\n"):
            try:
                data += self.connection.recv(1024)
                print(data)
            except socket.error as err:
                raise ClientError("Error reading data from socket", err)

        return data.decode('utf-8')

    def _send(self, data):

        try:
            self.connection.sendall(data)
        except socket.error as err:
            raise ClientError("Error sending data to server", err)

    def put(self, metric, value, timestamp=None):

        timestamp = timestamp or int(time.time())
        self._send(f"put {metric} {value} {timestamp}\n".encode())
        raw_data = self._read()

        if raw_data == 'ok\n\n':
            return
        raise ClientError(f'Server returns an error on put: {raw_data}')

    def get(self, key):

        self._send(f"get {key}\n".encode())
        try:
            raw_data = self._read()
        except Exception as err:
            raise ClientError(f'Ошибка с сервером метода get. Err: {err}')

        data = {}
        try:
            status, payload = raw_data.split("\n", 1)
        except Exception as err:
            raise ClientError(f'Получены неверные данные: {raw_data} Err: {err}')
        payload = payload.strip()

        if status != 'ok':
            raise ClientError(f'Server returns an error on get: {status}')

        if payload == '':
            return data

        try:

            for row in payload.splitlines():
                key, value, timestamp = row.split()
                if key not in data:
                    data[key] = []
                bisect.insort(data[key], (int(timestamp), float(value)))

        except Exception as err:
            raise ClientError('Server returns invalid data', err)

        return data

    def close(self):

        try:
            self.connection.close()
        except socket.error as err:
            raise ClientError("Error. Do not close the connection", err)