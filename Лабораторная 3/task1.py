class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        """Возвращает название книги"""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Не разрешает поменять название книги"""
        print("Название книги поменять нельзя")

    @property
    def author(self) -> str:
        """Возвращает автора книги"""
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        """Не разрешает поменять автора книги"""
        print("Автора книги поменять нельзя")


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге"""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге"""
        if not isinstance(new_pages, int) or isinstance(new_pages, bool):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительной величиной")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает длительность прослушивания"""
        return self._duration

    @duration.setter
    def duration(self, new_duration:  float) -> None:
        """Устанавливает длительность прослушивания"""
        if not isinstance(new_duration, float):
            raise TypeError("Длительность прослушивания должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность прослушивания должна быть положительной величиной")
        self._duration = new_duration