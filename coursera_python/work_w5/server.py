import asyncio
import threading


class DataBase:
    def __init__(self):
        self.base = {}
        self.mutex = threading.Lock()

    def put(self, key, timestamp, metric_value):
        with self.mutex:
            if key in self.base:
                self.base[key][timestamp] = metric_value
            else:
                self.base[key] = {timestamp: metric_value}

    def get(self, key):
        selection = {}
        with self.mutex:
            if key == "*":
                selection = self.base
            else:
                if key in self.base:
                    selection = {key: self.base[key]}
        return selection


class WrongCommand(Exception):
    def __init__(self, text):
        print("Wrong command: ", text)


class ClientServerProtocol(asyncio.Protocol):

    data_base = DataBase()

    def __init__(self):
        pass

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        try:
            # print("process_data: ", data)
            split_data = data.split()
            words_num = len(split_data)

            response = ""
            if words_num:
                command = split_data[0]
                if command == "get":
                    get_args = split_data[1:]
                    response = self.process_get_command(get_args)
                elif command == "put":
                    get_args = split_data[1:]
                    response = self.process_put_command(get_args)
                else:
                    raise WrongCommand(f"Неизвестная команда: {command}")
            else:
                raise WrongCommand(f"Отсутствует запрос: {data}")
        except WrongCommand:
            response = "error\nwrong command\n"
        response += "\n"
        # print("response: ", response.encode())
        return response

    def process_get_command(self, data):
        if len(data) == 1:
            response = "ok\n"
            selection = self.data_base.get(key=data[0])
            for key in selection:
                for timestamp in selection[key]:
                    metric = f"{key} {selection[key][timestamp]} {timestamp}\n"
                    response += metric
        else:
            raise WrongCommand(f"Не правильное число аргументов у команды get ({len(data)}): {data}")
        return response

    def process_put_command(self, data):
        if len(data) == 3:
            try:
                metric_value = float(data[1])
                timestamp = int(data[2])
            except (TypeError, ValueError):
                raise WrongCommand(f"Не правильные значения аргументов в команне put: {data}")
            self.data_base.put(key=data[0], metric_value=metric_value, timestamp=timestamp)
            response = "ok\n"
        else:
            raise WrongCommand(f"Не правильное число аргументов у команды put ({len(data)}): {data}")
        return response


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run_server('127.0.0.1', 8889)

