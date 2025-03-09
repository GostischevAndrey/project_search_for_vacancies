def test_filter_by_description(vacancy_object_1, vacancy_object_2, filter_sort_1):
    vacancies_list = [vacancy_object_1, vacancy_object_2]

    filtered_vacancies = filter_sort_1.filter_by_description(vacancies_list)

    assert len(filtered_vacancies) == 2

    assert filtered_vacancies[0] == vacancy_object_1


def test_filter_by_area(vacancy_object_1, vacancy_object_2, filter_sort_1):
    vacancies_list = [vacancy_object_1, vacancy_object_2]

    filtered_vacancies = filter_sort_1.filter_by_area(vacancies_list)

    assert len(filtered_vacancies) == 2


def test_filter_by_salary(vacancy_object_1, vacancy_object_2, filter_sort_1):
    vacancies_list = [vacancy_object_1, vacancy_object_2]

    filtered_vacancies = filter_sort_1.filter_by_salary(vacancies_list)

    assert len(filtered_vacancies) == 2


def test_sort_vacancies_by_salary(vacancy_object_1, vacancy_object_2, filter_sort_1):
    vacancies_list = [vacancy_object_1, vacancy_object_2]

    filter_vacancies = filter_sort_1.sort_vacancies_by_salary(vacancies_list)

    assert len(filter_vacancies)


def test_get_top_vacancies(vacancy_object_1, vacancy_object_2, filter_sort_1):
    vacancies_list = [vacancy_object_1, vacancy_object_2]

    top_vacancies = filter_sort_1.get_top_vacancies(vacancies_list)

    assert "Вакансия номер 1" in top_vacancies
    assert "Вакансия номер 2" not in top_vacancies


def test_get_top_vacancies_top_n_greater_than_list_length(vacancy_object_1, vacancy_object_2, filter_sort_2):
    vacancies_list = [vacancy_object_1, vacancy_object_2]

    top_vacancies = filter_sort_2.get_top_vacancies(vacancies_list)

    assert "Вакансия номер 1" in top_vacancies
    assert "Вакансия номер 2" in top_vacancies
    assert "Вакансия номер 3" not in top_vacancies
