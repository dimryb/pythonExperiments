import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying, car_type=''):
        self._valid = True
        self._brand = brand
        if brand == "":
            self._valid = False
        self._photo_file_name = photo_file_name
        self._car_type = car_type
        try:
            self._carrying = float(carrying)
        except ValueError:
            self._carrying = 0.0
            self._valid = False

        ext = self.get_photo_file_ext()
        if ext != ".jpg" and ext != ".jpeg" and ext != ".png" and ext != ".gif":
            self._photo_file_name = ""
            self._valid = False

    @property
    def brand(self):
        return self._brand

    @property
    def photo_file_name(self):
        return self._photo_file_name

    @property
    def carrying(self):
        return self._carrying

    @property
    def car_type(self):
        return self._car_type

    @property
    def valid(self):
        return self._valid

    def get_photo_file_ext(self):
        split_text = os.path.splitext(self._photo_file_name)
        try:
            ext = split_text[1]
        except IndexError:
            ext = ''
            self._valid = False

        return ext


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying, 'car')
        self._valid = super().valid
        try:
            self._passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            self._passenger_seats_count = 0
            self._valid = False

    @property
    def passenger_seats_count(self):
        return self._passenger_seats_count

    @property
    def valid(self):
        return self._valid


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying, 'truck')
        self._valid = super().valid
        self._body_whl = body_whl
        body_whls = body_whl.split("x")
        self._body_length = 0.0
        self._body_width = 0.0
        self._body_height = 0.0

        if (len(body_whls) > 3) or (len(body_whls) == 2):
            self._valid = False
            self._body_length = 0.0
            self._body_width = 0.0
            self._body_height = 0.0
        elif len(body_whls) == 3:
            try:
                self._body_length = float(body_whls[0])
                self._body_width = float(body_whls[1])
                self._body_height = float(body_whls[2])
            except ValueError:
                self._valid = False
                self._body_length = 0.0
                self._body_width = 0.0
                self._body_height = 0.0

    @property
    def body_whl(self):
        return self._body_whl

    @property
    def body_length(self):
        return self._body_length

    @property
    def body_width(self):
        return self._body_width

    @property
    def body_height(self):
        return self._body_height

    @property
    def valid(self):
        return self._valid

    def get_body_volume(self):
        return self._body_length*self._body_width*self._body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying, 'spec_machine')
        self._valid = super().valid
        self._extra = extra
        if extra == "":
            self._valid = False

    @property
    def extra(self):
        return self._extra

    @property
    def valid(self):
        return self._valid


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding="utf-8") as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                car_type = row[0]
                if car_type == 'car':
                    car = Car(brand=row[1], photo_file_name=row[3], carrying=row[5], passenger_seats_count=row[2])
                    if car.valid:
                        car_list.append(car)
                elif car_type == 'truck':
                    truck = Truck(brand=row[1], photo_file_name=row[3], carrying=row[5], body_whl=row[4])
                    if truck.valid:
                        car_list.append(truck)
                elif car_type == 'spec_machine':
                    spec_machine = SpecMachine(brand=row[1], photo_file_name=row[3], carrying=row[5], extra=row[6])
                    if spec_machine.valid:
                        car_list.append(spec_machine)
            except IndexError:
                pass
    return car_list
