import json

from src.base_json import JSONSaver


def test_write_and_read_file(tmpdir, vacancy_object_1):
    test_file = tmpdir.join("test_vacancies.json")
    saver = JSONSaver(filename=str(test_file))

    saver.write_file([vacancy_object_1])

    vacancies = saver.read_file()

    assert len(vacancies) == 1
    assert vacancies[0].name == "Python-разработчик"
    assert vacancies[0].salary == 256000
    assert vacancies[0].area == "Москва"
    assert vacancies[0].link == "https://hh.ru/vacancy/117783931"
    assert vacancies[0].description == "Разработка и поддержка микросервисной архитектуры на базе Python."


def test_clear_file(tmpdir, vacancy_object_1):
    test_file = tmpdir.join("test_vacancies.json")
    saver = JSONSaver(filename=str(test_file))

    saver.write_file([vacancy_object_1])

    saver.clear_file()

    with open(test_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data == []


def test_clear_error(tmpdir, mocker):
    test_file = tmpdir.join("test_vacancies.json")
    saver = JSONSaver(filename=str(test_file))

    mocker.patch("builtins.open", side_effect=IOError("File error"))

    saver.clear_file()


def test_write_file_error(tmpdir, mocker, vacancy_1):
    test_file = tmpdir.join("test_vacancies.json")
    saver = JSONSaver(filename=str(test_file))

    mocker.patch("builtins.open", side_effect=IOError("File error"))

    saver.write_file(vacancy_1)


def test_read_file_error(tmpdir, capsys):
    test_file = tmpdir.join("test_vacancies.json")
    test_file.write("invalid json")

    saver = JSONSaver(filename=str(test_file))

    saver.read_file()


def test_add_vacancy(vacancy_object_1, tmpdir):
    test_file = tmpdir.join("test_vacancies.json")

    saver = JSONSaver(filename=str(test_file))

    saver.add_vacancy(vacancy_object_1)

    with open(saver.filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["name"] == "Python-разработчик"
