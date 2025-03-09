from abc import ABC, abstractmethod
from typing import List

import requests


class BaseVacancyAPI(ABC):
    """Абстрактный родительский класс для подключения по API."""

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """Загружает вакансии по ключевому слову."""
        pass  # pragma: no cover

    @abstractmethod
    def get_vacancies(self) -> List:
        """Возвращает список вакансий."""
        pass  # pragma: no cover


class HeadHunterAPI(BaseVacancyAPI):
    """
    Класс для работы с API HeadHunter.
    Реализует методы для загрузки и получения вакансий.
    """

    def __init__(self):
        """Инициализация класса."""
        self._url = "https://api.hh.ru/vacancies"
        self._headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def load_vacancies(self, keyword: str, max_pages: int = 2):
        """Загружает вакансии по ключевому слову."""
        self.params["text"] = keyword
        self.params["page"] = 0
        self.vacancies = []

        while self.params["page"] < max_pages:
            try:
                response = requests.get(
                    self._url, headers=self._headers, params=self.params
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Ошибка при запросе к API: {e}")
                return
            else:
                data = response.json()
                vacancies = data.get("items", [])
                self.vacancies.extend(vacancies)
                self.params["page"] += 1

                if not vacancies:
                    break

    def get_vacancies(self, filter_func=None) -> List:
        """Возвращает список вакансий."""
        if filter_func:
            return list(filter(filter_func, self.vacancies))
        return self.vacancies


if __name__ == "__main__":  # pragma: no cover
    hh = HeadHunterAPI()
    hh.load_vacancies("Python")
    hh_vacancies = hh.get_vacancies()
    print(hh_vacancies)
