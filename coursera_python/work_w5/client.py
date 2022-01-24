import socket
import time


class ClientError(Exception):
    def __init__(self):
        pass


class Client:
    def __init__(self, adr, port, timeout=None):
        self.timeout = timeout
        try:
            self.sock = socket.create_connection((adr, port))
            self.sock.settimeout(timeout)
        except (ConnectionRefusedError, socket.timeout):
            raise ClientError

    @staticmethod
    def valid_data(data):
        if len(data) < 4:  # сильно короткий ответ
            print("data: ", data)
            raise ClientError
        if data[-1] != '\n' and data[-2] != '\n':  # не оканчивается на \n\n
            raise ClientError

    def get(self, request):
        request = "get {}\n".format(request)

        try:
            self.sock.sendall(request.encode("utf8"))
            data = self.sock.recv(1024).decode("utf-8")
        except socket.timeout:
            raise ClientError

        self.valid_data(data)

        lines = data.split('\n')
        result = {}
        if not len(lines):
            raise ClientError

        if lines[0] == 'ok':
            for line in lines[1:]:
                if not len(line):
                    continue
                split_metric_line = line.split()
                if len(split_metric_line) == 3:
                    key = split_metric_line[0]
                    try:
                        timestamp = int(split_metric_line[2])
                        metric_value = float(split_metric_line[1])
                    except ValueError:
                        raise ClientError

                    if key in result:
                        result[key] += [(timestamp, metric_value)]
                    else:
                        result[key] = [(timestamp, metric_value)]
                    result[key].sort()
                else:
                    raise ClientError
        elif lines[0] == 'error':
            raise ClientError
        else:
            raise ClientError

        return result

    def put(self, metric, value, timestamp=None):
        if not timestamp:
            timestamp = int(time.time())

        request = "put {} {} {}\n".format(str(metric), str(value), str(timestamp))

        self.sock.sendall(request.encode("utf8"))
        data = self.sock.recv(1024).decode("utf-8")

        self.valid_data(data)
        lines = data.split('\n')

        if lines[0] != 'ok':
            raise ClientError
        return data
