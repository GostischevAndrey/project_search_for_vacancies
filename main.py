from src.base_json import JSONSaver
from src.base_api import HeadHunterAPI
from src.utils import FilterSortVacancies


# Функция для взаимодействия с пользователем
def user_interaction():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON
    hh_api.load_vacancies(search_query)
    hh_vacancies = hh_api.get_vacancies()

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.write_file(hh_vacancies)
    print(f"Вакансии в количестве {len(hh_vacancies)} успешно загружены и записаны в файл")

    # Обращение к пользователю. Сбор информации
    filter_word = input("Введите ключевое слово для фильтрации вакансий по описанию: ")
    filter_area = input("Введите город для фильтрации вакансий по местоположению: ")
    filter_salary = int(input("Введите желаемую минимальную зарплату: "))
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    print("")

    read_vacs_from_json = json_saver.read_file()
    # Создание экземпляра класса фильтрации и сортировки вакансий
    filtered_obj = FilterSortVacancies(filter_word, filter_area, filter_salary, top_n)

    filtered_by_description = filtered_obj.filter_by_description(read_vacs_from_json)
    print(f"Отфильтровано {len(filtered_by_description)} вакансий по описанию")
    filtered_by_area = filtered_obj.filter_by_area(filtered_by_description)
    print(f"Отфильтровано {len(filtered_by_area)} вакансий по местоположению")
    filtered_by_salary = filtered_obj.filter_by_salary(filtered_by_area)
    print(f"Отфильтровано {len(filtered_by_salary)} вакансий по зарплате\n")

    sorted_by_salary = filtered_obj.sort_vacancies_by_salary(filtered_by_salary)

    top_vacancies = filtered_obj.get_top_vacancies(sorted_by_salary)

    print(f"Топ {top_n} вакансий:\n{top_vacancies}\n")

    user_input = input("Очистить файл с вакансиями? (да / нет): ").lower()
    if user_input == "да":
        json_saver.clear_file()


if __name__ == "__main__":
    user_interaction()
