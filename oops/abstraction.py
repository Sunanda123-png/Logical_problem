from abc import ABC, abstractmethod


class Doctor(ABC):
    def __init__(self, name):
        self.name = name

    def hospital(self):
        print("Aiims")

    @abstractmethod
    def speciality(self):
        pass


class Surgen(Doctor):
    def speciality(self):
        print(f'{self.name} is a surgen')


s = Surgen("ram")
s.speciality()
s.hospital()
