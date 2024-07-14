from settings import CURRENCY_MATCH_RUB
from src.vacancy import Vacancy


def filter_vacancies_by_keyword(filter_words: list[str], *vacancies: Vacancy) -> list[Vacancy]:
    """
    Фильтрует список объектов Vacancy по ключевым словам.
    :param filter_words: cписок слов для поиска по полям name, employer, requirement, responsibility
    :param vacancies: список объектов Vacancy
    :return: отфильтрованный список объектов Vacancy
    """
    # если список слов для фильтрования не пустой производим фильтрацию
    if filter_words:
        keywords_lower = [keyword.lower() for keyword in filter_words]
        filtered_vacancies = [
            vacancy for vacancy in vacancies
            if any(
                keyword in vacancy.name.lower() or
                keyword in vacancy.employer.lower() or
                keyword in vacancy.requirement.lower() or
                keyword in vacancy.responsibility.lower()
                for keyword in keywords_lower
            )
        ]

        return filtered_vacancies
    else:
        return list(vacancies)


def get_vacancies_by_salary(low_salary: int, high_salary: int, *vacancies: Vacancy) -> list[Vacancy]:
    """
    Фильтрует список объектов Vacancy по зарплатам.
    :param low_salary: int
    :param high_salary: int
    :param vacancies: список объектов Vacancy
    :return: отфильтрованный список объектов Vacancy
    """
    filtered_vacancies = [
        vacancy for vacancy in vacancies
        if (vacancy.salary_from and high_salary >= vacancy.salary_from) or
           (vacancy.salary_to and low_salary <= vacancy.salary_to)
    ]

    return filtered_vacancies


def get_top_vacancies(count: int, *vacancies: Vacancy) -> list[Vacancy]:
    """
    Выводит список отсортированный по зарплате в количестве 'count' вакансий
    :param count: количество элементов списка
    :param vacancies: список объектов Vacancy
    :return: список объектов Vacancy обрезанный по количеству элементов
    """
    new_vacancies_list = list(vacancies)
    new_vacancies_list.sort(reverse=True)
    output_vacancies_list = new_vacancies_list[:count]

    return output_vacancies_list


def print_vacancies(*vacancies: Vacancy) -> None:
    """
    Вывод на печать вакансий построчно
    :param vacancies:
    """
    for vacancy in vacancies:
        print(vacancy)
        print('-'*50)
