import sys

from settings import PARSING_PAGES_COUNT_FROM_HH, JSON_STORAGE
from src.db_connector import JSONHandler
from src.filters import filter_vacancies_by_keyword, get_vacancies_by_salary, get_top_vacancies, print_vacancies
from src.parser_classes import HH
from requests.exceptions import ConnectionError, Timeout

from src.vacancy import Vacancy


def user_interaction():
    search_query = input("Введите поисковый запрос для поиска вакансий: ")

    try:
        top_n = int(input("Введите количество вакансий для отображения или нажмите 'Enter': "))
    except ValueError:
        print("Будут выведены все доступные вакансии")
        top_n = PARSING_PAGES_COUNT_FROM_HH * 100

    filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел или нажмите 'Enter': ").split()

    try:
        low_salary, high_salary = map(int, input("Введите диапазон зарплат в формате 100000 - 150000 "
                                                 "или нажмите 'Enter': ")
                                      .replace(" ", "").split('-'))
    except ValueError:
        print("Будут выведены все доступные вакансии без учета зарплаты")
        low_salary = 0
        high_salary = sys.maxsize

    # создаем объект парсера вакансий с HH.ru
    hh = HH(PARSING_PAGES_COUNT_FROM_HH)

    # собираем данные через API. В случае ошибки запроса, заканчиваем работу программы
    try:
        vacancies = hh.load_vacancies(search_query)
    except ConnectionError:
        print("Нет соединения с сайтом.")
        return
    except Timeout:
        print("Запрос занял слишком много времени.")
        return

    # создаем список объектов из списка словарей
    vacancies_list = Vacancy.cast_to_object_list(vacancies)
    # создаем класс для работы с файлом
    json_handler = JSONHandler(vacancies_list)
    # сохраняем данные в нужном формате в файл
    json_handler.save(JSON_STORAGE)
    # получаем данные из файла и работаем с ними без запросов к API
    vacancies_list_from_file = json_handler.read_data(JSON_STORAGE)

    # фильтруем данные по нашим запросам
    filtered_vacancies = filter_vacancies_by_keyword(filter_words, *vacancies_list_from_file)
    ranged_vacancies = get_vacancies_by_salary(low_salary, high_salary, *filtered_vacancies)
    top_vacancies = get_top_vacancies(top_n, *ranged_vacancies)

    print("\n Вакансии по Вашему запросу:")
    print_vacancies(*top_vacancies)


if __name__ == "__main__":
    user_interaction()
