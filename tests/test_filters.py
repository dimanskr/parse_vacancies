from src.filters import filter_vacancies_by_keyword, get_vacancies_by_salary, get_top_vacancies
from src.vacancy import Vacancy


def test_filter_vacancies_by_keyword(list_objects):
    filtered_vacancies = filter_vacancies_by_keyword(['Разработчик1', 'Умение6'], *list_objects)

    assert len(filtered_vacancies) == 2
    assert filtered_vacancies[0].name == 'Разработчик1'


def test_filter_vacancies_by_keyword_empty_keywords(list_objects):
    filtered_vacancies = filter_vacancies_by_keyword([], *list_objects)

    assert len(filtered_vacancies) == 6
    assert all(isinstance(vacancy, Vacancy) for vacancy in filtered_vacancies)


def test_filter_vacancies_by_keyword_no_matches(list_objects):
    filtered_vacancies = filter_vacancies_by_keyword(['Python'], *list_objects)

    assert len(filtered_vacancies) == 0


def test_get_vacancies_by_salary(list_objects):
    filtered_vacancies = get_vacancies_by_salary(10000, 30000, *list_objects)

    assert len(filtered_vacancies) == 5


def test_get_top_vacancies(list_objects):
    top_vacancies = get_top_vacancies(2, *list_objects)

    assert len(top_vacancies) == 2
    assert top_vacancies[0].name == 'Разработчик3'


def test_get_top_vacancies_less_than_count(list_objects):
    top_vacancies = get_top_vacancies(10, *list_objects)

    assert len(top_vacancies) == 6


def test_get_top_vacancies_empty_list():
    top_vacancies = get_top_vacancies(2)

    assert len(top_vacancies) == 0


