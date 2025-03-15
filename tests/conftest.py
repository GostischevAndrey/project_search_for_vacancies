import pytest

from src.utils import FilterSortVacancies
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1():
    return {
        "name": "Python-разработчик",
        "area": {"name": "Москва"},
        "salary": {"from": 256000},
        "alternate_url": "https://hh.ru/vacancy/117783931",
        "snippet": {"responsibility": "Разработка и поддержка микросервисной архитектуры на базе Python."}
    }


@pytest.fixture
def vacancy_object_1(vacancy_1):
    return Vacancy(vacancy_1)


@pytest.fixture
def vacancy_2():
    return {
        "name": "Web-разработчик",
        "area": {"name": "Москва"},
        "salary": {"from": 100000},
        "alternate_url": "https://hh.ru/vacancy/117730185",
        "snippet": {"responsibility": "Работа с WordPress: наполнение контентом, редактирование страниц."}
    }


@pytest.fixture
def vacancy_object_2(vacancy_2):
    return Vacancy(vacancy_2)


@pytest.fixture
def filter_sort_1():
    return FilterSortVacancies(
        filter_word="",
        filter_area="",
        filter_salary=0,
        top_n=1
    )


@pytest.fixture
def filter_sort_2():
    return FilterSortVacancies(
        filter_word="",
        filter_area="",
        filter_salary=0,
        top_n=3
    )
