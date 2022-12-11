# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class SoundInterface:
    """Класс "звуковая карта" с двумя аттрибутами: максимальная частота дискретизации и кол-во входов
    >>> sound = SoundInterface(96000, 3)
    
    """
    def __init__(self, frequency: int, inputs: int):
        self.frequency = frequency
        self.inputs = inputs
        if not isinstance(frequency, int):
            raise TypeError
        if not isinstance(inputs, int):
            raise TypeError

    def connect_mic(self):
        # подключить микрофон
        ...

    def switch_phantom_power(self):
        # включить фантомное питание 48V для микрофона на звуковой карте
        ...


class GoogleDrive:
    """ Класс "google диск" с двумя атрибутамии - максимальный размер хранилища и используемое место
    >>> drive = GoogleDrive(15, 5.8)
    
    """
    def __init__(self, storage: Union[int, float], used_memory: Union[int, float],):
        self.storage = storage
        self.used_memory = used_memory
        if not isinstance(storage, (int, float)):
            raise TypeError
        if not isinstance(used_memory, (int, float)):
            raise TypeError

    def add_files(self, files:Union[int, float]):
        # загрузить файлы на диск
        if not isinstance(files, (int, float)):
            raise TypeError
        if (files + self.used_memory) > self.storage:
            raise ValueError
        else:
            self.used_memory += files

    def delete_files(self, files:Union[int, float]):
        # удалить файлы с диска
        if not isinstance(files, (int, float)):
            raise TypeError
        if files > self.used_memory:
            raise ValueError
        else:
            self.used_memory -= files


class Elevator:
    """ Класс "лифт" c двумя атрибутами: максимальная вместимость и кол-во человек внутри
    >>> elev = Elevator(12, 7)
    
    """
    def __init__(self, capacity: int, people_inside: int):
        if not isinstance(capacity, int):
            raise TypeError
        if not isinstance(people_inside, int):
            raise TypeError
        self.capacity = capacity
        self.people_inside = people_inside

    def add(self, people: int):
        # Пустить в лифт ещё несколько человек, если достаточно места
        if not isinstance(people, int):
            raise TypeError
        if not (self.capacity - self.people_inside) >= people:
            raise ValueError
        else:
            self.capacity -= people
            self.people_inside += people

    def get(self, people: int):
        # Выпустить несколько человек из лифта, если они приехали на свой этаж
        if not isinstance(people, int):
            raise TypeError
        if not self.people_inside > people:
            raise ValueError
        else:
            self.people_inside -= self.people


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
doctest.testmod()


