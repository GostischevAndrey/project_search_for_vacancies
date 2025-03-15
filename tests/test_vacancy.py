def test_vacancy_init(vacancy_object_1):
    assert vacancy_object_1.name == "Python-разработчик"
    assert vacancy_object_1.area == "Москва"
    assert vacancy_object_1.salary == 256000
    assert vacancy_object_1.link == "https://hh.ru/vacancy/117783931"
    assert vacancy_object_1.description == "Разработка и поддержка микросервисной архитектуры на базе Python."


def test_vacancy_str(vacancy_object_1):
    assert str(vacancy_object_1) == (
        'Вакансия: Python-разработчик, Ссылка: https://hh.ru/vacancy/117783931, Зарплата: 256000, '
        'Описание: Разработка и поддержка микросервисной архитектуры на базе Python., Место: Москва'
    )


def test_vacancy_comparison(vacancy_object_1, vacancy_object_2):
    assert vacancy_object_1 > vacancy_object_2
    assert vacancy_object_1 >= vacancy_object_2
    assert vacancy_object_2 < vacancy_object_1
    assert vacancy_object_2 <= vacancy_object_1
