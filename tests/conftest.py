import pytest
from src.parser_classes import HH
from src.vacancy import Vacancy


@pytest.fixture
def hh():
    return HH(pages_count=3)


@pytest.fixture
def list_objects():
    return [
        Vacancy(vacancy_id=1, name='Разработчик1', url='https://hh.ru/vacancy/1', employer='Яндекс1',
                requirement='Умение1', responsibility='Работать1', salary_from='100000', salary_to='200000',
                currency='RUR'),
        Vacancy(vacancy_id=2, name='Разработчик2', url='https://hh.ru/vacancy/2', employer='Яндекс2',
                requirement='Умение2', responsibility='Работать2', salary_from='10000', salary_to='20000',
                currency='RUR'),
        Vacancy(vacancy_id=3, name='Разработчик3', url='https://hh.ru/vacancy/3', employer='Яндекс3',
                requirement='Умение3', responsibility='Работать3', salary_from='11000', salary_to='22000',
                currency='USD'),
        Vacancy(vacancy_id=4, name='Разработчик4', url='https://hh.ru/vacancy/4', employer='Яндекс4',
                requirement='Умение4', responsibility='Работать4', salary_from='None', salary_to='None',
                currency='None'),
        Vacancy(vacancy_id=5, name='Разработчик5', url='https://hh.ru/vacancy/5', employer='Яндекс5',
                requirement='Умение5', responsibility='Работать5', salary_from='None', salary_to='50000',
                currency='RUR'),
        Vacancy(vacancy_id=6, name='Разработчик6', url='https://hh.ru/vacancy/6', employer='Яндекс6',
                requirement='Умение6', responsibility='Работать6', salary_from='10000', salary_to='None',
                currency='RUR'),
    ]


@pytest.fixture
def vacancy_for_init():
    return {
        'vacancy_id': '1',
        'name': 'Developer',
        'url': 'https://hh.ru/vacancy/1',
        'employer': 'Corporation',
        'requirement': 'Python skills',
        'responsibility': 'Develop Python applications',
        'salary_from': 100000,
        'salary_to': 200000,
        'currency': 'RUR',
    }


