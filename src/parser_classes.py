import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Абстрактный класс для загрузки вакансий
    """
    @abstractmethod
    def load_vacancies(self, keyword: str) -> list:
        """
        Абстрактный метод загрузки вакансий
        """
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self, pages_count: int):
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self._params = {'text': '', 'page': 0, 'per_page': 100}
        self._vacancies = []
        self._pages_count = pages_count

    def load_vacancies(self, keyword: str) -> list[dict]:
        """
        Метод загрузки вакансий с HH.ru через API
        :param keyword: str
        :return self._vacancies: list[dict]
        """
        self._params['text'] = keyword
        while self._params.get('page') != self._pages_count:
            response = requests.get(self._url, headers=self._headers, params=self._params, timeout=10)
            if response.status_code == 200:
                vacancies = response.json()['items']
                self._vacancies.extend(vacancies)
                self._params['page'] += 1
        return self._vacancies

    def __str__(self):
        return f"Класс для работы с API {self._url}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(url='{self._url}', headers='{self._headers}', params='{self._params}', "
                f"vacancies[:2]={self._vacancies[:2]}, pages_count={self._pages_count}")
