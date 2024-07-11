# Функция для взаимодействия с пользователем
from settings import PARSING_PAGES_COUNT_FROM_HH
from src.parser_classes import HH
from requests.exceptions import ConnectionError, Timeout


def user_interaction():
    # platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
    #
    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)
    hh = HH(PARSING_PAGES_COUNT_FROM_HH)

    try:
        vacancies = hh.load_vacancies(search_query)
    except ConnectionError:
        print("Нет соединения с сайтом.")
    except Timeout:
        print("Запрос занял слишком много времени.")


if __name__ == "__main__":
    user_interaction()
