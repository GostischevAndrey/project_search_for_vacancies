import json
import os
from abc import ABC, abstractmethod
from typing import List, Optional

from config import DATA_DIR
from src.vacancy import Vacancy


class Worker(ABC):
    """Абстрактный родительский класс для чтения и записи файла"""

    @abstractmethod
    def read_file(self) -> List[Vacancy]:
        pass  # pragma: no cover

    @abstractmethod
    def write_file(self, vacs_obj: List[Vacancy]) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def clear_file(self) -> None:
        pass  # pragma: no cover


class JSONSaver(Worker):
    """
    Класс для чтения из файла, записи в файл списка вакансий
    Класс Worker является родительским классом
    """

    filename_value = "vacancies.json"

    def __init__(self, filename: Optional[str] = None):
        self.vacs_list: List[Vacancy] = []
        self.__filename = os.path.join(DATA_DIR, filename or self.filename_value)

    @property
    def filename(self) -> str:
        return self.__filename

    def read_file(self) -> List[Vacancy]:
        """Функция для чтения файла. Проверяет, есть ли файл. И, если есть, сохраняет список объектов."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="UTF-8") as f:
                    vacs = json.load(f)
                self.vacs_list = [Vacancy(i) for i in vacs]
            except (json.JSONDecodeError, IOError) as e:
                print(f"Ошибка при чтении файла: {e}")
        return self.vacs_list

    def write_file(self, vacs_obj: List[Vacancy]) -> None:
        """Функция для записи списка вакансий в файл. Принимает список объектов класса Vacancy."""
        vacs_list = []
        for vac in vacs_obj:
            if isinstance(vac, Vacancy):
                vacs_list.append(
                    {
                        "name": vac.name,
                        "alternate_url": vac.link,
                        "salary": {"from": vac.salary},
                        "snippet": {"responsibility": vac.description},
                        "area": {"name": vac.area},
                    }
                )
            else:
                vacs_list.append(vac)
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(vacs_list, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Ошибка при записи файла: {e}")

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Функция для добавления вакансии в файл."""
        self.vacs_list.append(vacancy)
        self.write_file(self.vacs_list)

    def clear_file(self) -> None:
        """Функция для очистки файла с вакансиями."""
        self.vacs_list = []
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write("[]")
        except IOError as e:
            print(f"Ошибка при очистке файла: {e}")


if __name__ == "__main__":  # pragma: no cover
    saver = JSONSaver()
    vacs = saver.read_file()
    print(vacs)
