from src.mixins import CleanTagsMixin
from src.utils import currency_to_rub_coefficient as currency_converter


class Vacancy(CleanTagsMixin):
    """
    Класс вакансии с HH.ru
    """

    def __init__(self, vacancy_id: str, name: str, url: str, employer: str, requirement: str, responsibility: str,
                 salary_from, salary_to, currency):
        self._id = vacancy_id
        self._name = name
        self._url = url
        self._employer = self.clean_tags(employer)
        self._requirement = self.clean_tags(requirement)
        self._responsibility = self.clean_tags(responsibility)
        self._salary_from = salary_from if salary_from else None
        self._salary_to = salary_to if salary_to else None
        self._currency = currency if currency else None

    @property
    def vacancy_id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name if self._name else ''

    @property
    def url(self) -> str:
        return self._url

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def salary(self) -> str:
        """
        Метод вывода строки диапазона зарплат в формате: 1000 - 100000 RUR
        :return: str
        """
        if not self._currency:
            return "зарплата не указана"

        if self.salary_from:
            sal_from = f" от {self.salary_from}"
        else:
            sal_from = ""

        if self.salary_to:
            sal_to = f" до {self.salary_to}"
        else:
            sal_to = ""

        return f"зарплата{sal_from}{sal_to} руб."

    @property
    def salary_from(self) -> int | None:
        """
        Нижняя граница зарплаты, переведенная в рубли
        :return: int | None
        """
        try:
            tmp_salary_from = int(self._salary_from)
        except TypeError:
            tmp_salary_from = None
        except ValueError:
            tmp_salary_from = None
        if tmp_salary_from:
            return int(float(tmp_salary_from) * currency_converter(self._currency))
        else:
            return None

    @property
    def salary_to(self) -> int | None:
        """
        Верхняя граница зарплаты, переведенная в рубли
        :return: int | None
        """
        try:
            tmp_salary_to = int(self._salary_to)
        except TypeError:
            tmp_salary_to = None
        except ValueError:
            tmp_salary_to = None
        if tmp_salary_to:
            return int(float(tmp_salary_to) * currency_converter(self._currency))
        else:
            return None

    @property
    def requirement(self):
        return self._requirement if self._requirement else 'не указаны'

    @property
    def responsibility(self):
        return self._responsibility if self._responsibility else 'не указаны'

    @property
    def employer(self):
        return self._employer if self._employer else ''

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list:
        """
        Метод класса для преобразования загруженного списка словарей в список объектов Vacancy.
        :param vacancies: list[dict]
        :return: list[Vacancy]
        """
        objects = []
        for vacancy_dict in vacancies:
            # Получаем данные о зарплате
            salary_data = vacancy_dict.get('salary')

            # Создаём объект Vacancy
            vacancy_obj = cls(
                vacancy_id=vacancy_dict['id'],
                name=vacancy_dict['name'],
                url=vacancy_dict['alternate_url'],
                employer=vacancy_dict['employer']['name'],
                requirement=vacancy_dict['snippet']['requirement'],
                responsibility=vacancy_dict['snippet']['responsibility'],
                salary_from=salary_data.get('from') if salary_data else None,
                salary_to=salary_data.get('to') if salary_data else None,
                currency=salary_data.get('currency') if salary_data else None
            )
            objects.append(vacancy_obj)
        return objects

    def to_dict(self) -> dict:
        """
        Метод преобразования экземпляра объекта в словарь
        :return: dict
        """
        return {
            'vacancy_id': self._id,
            'name': self._name,
            'url': self._url,
            'employer': self._employer,
            'requirement': self._requirement,
            'responsibility': self._responsibility,
            'salary_from': self._salary_from,
            'salary_to': self._salary_to,
            'currency': self._currency
        }

    def __str__(self):
        return (f"Вакансия: {self._name} от \"{self._employer}\", ссылка: {self._url} \n"
                f"{self.salary.capitalize()} \n"
                f"Требования: {self.requirement} \n"
                f"Обязанности: {self.responsibility}")

    def __repr__(self):
        return (f"{self.__class__.__name__}(vacancy_id={self._id}, name='{self._name}', url='{self._url}', "
                f"employer='{self._employer}', requirement='{self._requirement}', "
                f"responsibility='{self._responsibility}', salary_from='{self._salary_from}', "
                f"salary_to='{self._salary_to}', currency='{self._currency}',)")

    def __lt__(self, other):
        # сравниваем верхний порог зарплат при наличии
        if self.salary_to and other.salary_to:
            return self.salary_to < other.salary_to
        # сравниваем верхний порог зарплат с нижним при наличии
        elif self.salary_to and other.salary_from:
            return self.salary_to < other.salary_from
        # если первое значение отсутствует, то оно автоматически меньше
        elif self.salary_to is None and other.salary_to:
            return True
        # сравниваем нижний порог зарплат при наличии
        elif self.salary_from and other.salary_from:
            return self.salary_from < other.salary_from
        # если первое значение отсутствует, то оно автоматически меньше
        elif self.salary_from is None and other.salary_from:
            return True

    def __eq__(self, other):
        # если верхние пороги зарплат равны
        if self.salary_to == other.salary_to:
            return True
        # верхних порогов зарплат нет, тогда сравниваем нижние
        elif self.salary_from is None and other.salary_from is None:
            return self.salary_from == other.salary_from
        # если нет данных по зарплатам, тогда они равны
        elif not self._currency:
            return self.salary_from == other.salary_form
