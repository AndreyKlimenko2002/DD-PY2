import doctest

class TennisEquipment:
    """
        Создание и подготовка к работе  базового класса "Инвентарь теннисиста"
    :param brand: производитель предмета для тенниса
    :param model: вид предмета для тенниса
    :param weight: вес предмета для тенниса
    """
    def __init__(self, brand: str, model: str, weight: int):
        self.brand = brand
        self.model = model
        self.weight = weight

    def __str__(self)->str:
        return f"Производитель {self.brand}. Вид предмета {self.model}. Вес предмета {self.weight}"

    def __repr__(self) ->str:
        return f"{self.__class__.__name__} brand={self.brand!r}, model={self.model!r}, weight={self.weight}"

    def weight_suitable(self, weight: int):
        """
        Функция, которая проверяет, что вес предмета из инвентаря теннисиста типа int
        :param weight: Вес предмета
        :raise ValueError: Если вес указан тип не int, то вызываем ошибку
        Примеры:
        >>> subject = TennisEquipment("Babolat","рюкзак", 800)
        >>> subject.weight_suitable(800)
        """
        if not isinstance(weight, int):
            raise TypeError("Вес предмета для тенниса  должен быть типа int")

    def weight_total(self, weight:int):
        """
        Функция weight_total проверяет, не превышает ли вес предмета для тенниса 1000 гр
        :param weight: Вес предмета
        :raise ValueError: Если вес больше допустимого, то вызываем ошибку ValueError
        """
        if self.weight >= 1000:
            raise ValueError("Вес предмета не может быть более 1000 граммов")

class Ball(TennisEquipment):
    """
    Создание дочернего класса "Мяч".
    :param brand: производитель предмета для тенниса
    :param model: вид предмета для тенниса
    :param weight: вес предмета для тенниса
    :param diameter_of_ball: диаметр мяча
     """
    def __init__(self, brand: str, model: str, weight: int, diameter_of_ball: float):
        """
        Расширяем конструктор базового класса, так как у мяча есть дополнительный атрибут - диаметр (diameter_of_ball).
        """
        super().__init__(brand, model, weight)
        self.diameter_of_ball = diameter_of_ball

    def __str__(self)->str:
        """
        Перегружаем  str, так как у мяча есть дополнительный атрибут - диаметр, и это надо отобразить в str
        """
        return f"Производитель {self.brand}. Вид предмета {self.model}. Вес предмета {self.weight}. Диаметр мяча {self.diameter_of_ball}"

    def __repr__(self) -> str:
        """
        Перегружаем  repr так как у мяча есть дополнительный атрибут - диаметр, и это надо отобразить в repr
        """
        return f"{self.__class__.__name__} brand={self.brand!r}, model={self.model!r}, weight={self.weight}, diameter_of_ball={self.diameter_of_ball}"

    def weight_total(self, weight: int):
        """
        Перегружаем функцию weight_total, так как у мяча вес не может быть больше 60 гр
        """
        if self.weight >= 60:
            raise ValueError ("Вес мяча не может быть более 60 граммов")

    @property
    def diameter_of_ball(self):
        """Возвращает диаметр мяча"""
        return self._diameter_of_ball

    @diameter_of_ball.setter
    def diameter_of_ball (self, new_diameter_of_ball: float) -> None:
        """Устанавливает диаметр мяча."""
        if not isinstance(new_diameter_of_ball, float):
            raise TypeError ("Диаметр мяча должен быть типа float")
        if not new_diameter_of_ball >= 1:
            raise ValueError ("Диаметр мяча должен быть положительным числом")
        self._diameter_of_ball = new_diameter_of_ball


class Bat(TennisEquipment):
    """
    Дочерний класс "Ракетки"
    :param brand: производитель предмета для тенниса
    :param model: вид предмета для тенниса
    :param weight: вес предмета для тенниса
    :param length: длина ракеток
    """

    def __init__(self, brand: str, model: str, weight: int, length_of_bats: int):
        """Расширяем  конструктор базового класса, так как у ракеток есть дополнительный атрибут - длина (lenght_of_bats)
        """
        super().__init__(brand, model, weight)
        self.length_of_bats = length_of_bats

    def __str__(self)->str:
        """
        Перегружаем  str, так как у ракеток есть дополнительный атрибут lenght_of_bats, и его надо прописать в str
        """
        return f"Производитель {self.brand}. Вид предмета {self.model}. Вес предмета {self.weight}. Длина ракеток {self.length_of_bats}"

    def __repr__(self) -> str:
        """
        Перегружаем  repr, так как у ракеток есть дополнительный атрибут lenght_of_bats, и его надо прописать в repr
        """
        return f"{self.__class__.__name__} brand={self.brand!r}, model={self.model!r}, weight={self.weight}, length_of_bats={self.length_of_bats}"

    def weight_total(self, weight: int):
        """
        Перегружаем  weight_total так как вес ракетки не должен быть более 340 гр.
        """
        if self.weight >= 340:
            raise ValueError("Вес одной ракетки не может быть более 340 граммов")

    def suitable_age(self):
        """
        Метод suitable_age определяет, на какой возраст расчитаны данные ракетки
        53-57 см -  от 4 до 6 лет
        58-62 см - от 7 до 11 лет
        63-67 см - от 12 до 16 лет
        68 см и более -  спортсмены старше 16 лет
        """

        if 53 <= self.length_of_bats <= 57:
            print("Ракетки для теннисистов от 4 до 6 лет ")
        if 58 <= self.length_of_bats <= 62:
            print("Ракетки для теннисистов от 7 до 11 лет ")
        if 63 <= self.length_of_bats <= 67:
            print("Ракетки для теннисистов от 12 до 16 лет ")
        if self.length_of_bats >= 68:
            print("Ракетки для теннисистов от 16 лет и старше ")


print(Ball("Head","Tour 4b 570704", 59, 6.7))
print(Bats("Dunlop","CX 200 LS", 340, 68))
print(repr(Ball("Head","Tour 4b 570704", 59, 6.7)))
print(repr(Bats("Dunlop","CX 200 LS", 340, 68)))
bats_ = Bats("Dunlop","CX 200 LS", 340, 68)
bats_.suitable_age()

ball = Ball("Dunlop","Tour 4b 570704", 59, 6.7)
print(ball.diameter_of_ball)  # вызываем как атрибут, но срабатывает метод
ball.diameter_of_ball = 6.8  # присваиваем значение атрибуту, но срабатывает метод
print(ball.diameter_of_ball)

if __name__ == "__main__":
    doctest.testmod()  # тестируем примеры, которые находятся в документации