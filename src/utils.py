import re
from typing import List


class FilterSortVacancies:
    """Класс для фильтрации, сортировки и вывода топ вакансий."""

    def __init__(self, filter_word, filter_area, filter_salary, top_n):
        self.filter_word = filter_word
        self.filter_area = filter_area
        self.filter_salary = filter_salary
        self.top_n = top_n

    def filter_by_description(self, vacancies_list: List) -> List:
        """Функция для фильтрации вакансий по заданному слову в описании."""
        return [vac for vac in vacancies_list if self.filter_word.lower() in vac.description.lower()]

    def filter_by_area(self, vacancies_list: List) -> List:
        """Функция для фильтрации вакансий по заданному городу."""
        filtered_vacancies_list = []
        for vac in vacancies_list:
            if re.findall(self.filter_area, vac.area, re.IGNORECASE):
                filtered_vacancies_list.append(vac)
        return filtered_vacancies_list

    def filter_by_salary(self, vacancies_list: List) -> List:
        """Функция для фильтрации вакансий по заданной зарплате."""
        filtered_vacancies_list = []
        for vac in vacancies_list:
            if vac.salary >= self.filter_salary:
                filtered_vacancies_list.append(vac)
        return filtered_vacancies_list

    @staticmethod
    def sort_vacancies_by_salary(vacancies_list: List) -> List:
        """Функция для сортировки вакансий по зарплате."""
        vacancies_list.sort(key=lambda x: x.salary, reverse=True)
        return vacancies_list

    def get_top_vacancies(self, vacancies_list: List) -> str:
        """Функция для получения топ N вакансий."""
        top_vacancies = ""
        if self.top_n < len(vacancies_list):
            for i in range(self.top_n):
                top_vacancies += (
                    f"Вакансия номер {i + 1}:\n{str(vacancies_list[i])}\n\n"
                )
        else:
            for i in range(len(vacancies_list)):
                top_vacancies += (
                    f"Вакансия номер {i + 1}:\n{str(vacancies_list[i])}\n\n"
                )
        return top_vacancies
