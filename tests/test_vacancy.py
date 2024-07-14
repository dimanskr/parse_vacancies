from src.vacancy import Vacancy


def test_vacancy_initialization(vacancy_for_init):
    vacancy = Vacancy(**vacancy_for_init)

    assert vacancy.vacancy_id == '1'
    assert vacancy.name == 'Developer'
    assert vacancy.url == 'https://hh.ru/vacancy/1'
    assert vacancy.employer == 'Corporation'
    assert vacancy.requirement == 'Python skills'
    assert vacancy.responsibility == 'Develop Python applications'
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 200000
    assert vacancy.currency == 'RUR'


def test_salary_property_no_currency(vacancy_for_init):
    vacancy_for_init['currency'] = None
    vacancy = Vacancy(**vacancy_for_init)

    assert vacancy.salary == 'зарплата не указана'


def test_salary_property(vacancy_for_init):
    vacancy = Vacancy(**vacancy_for_init)

    salary_str = 'зарплата от 100000 до 200000 руб.'
    assert vacancy.salary == salary_str


def test_cast_to_object_list():
    vacancies_data_from_api = [
        {
            'id': '1',
            'name': 'Python Developer',
            'alternate_url': 'https://hh.ru/vacancy/1',
            'employer': {'name': 'Corporation1'},
            'snippet': {
                'requirement': 'Python skills',
                'responsibility': 'Develop Python applications'
            },
            'salary': {
                'from': 100000,
                'to': 200000,
                'currency': 'RUR'
            }
        },
        {
            'id': '2',
            'name': 'Java Developer',
            'alternate_url': 'https://hh.ru/vacancy/2',
            'employer': {'name': 'Corporation2'},
            'snippet': {
                'requirement': 'Java skills',
                'responsibility': 'Develop Java applications'
            },
            'salary': {
                'from': 150000,
                'to': 250000,
                'currency': 'RUR'
            }
        }
    ]

    vacancies = Vacancy.cast_to_object_list(vacancies_data_from_api)

    assert len(vacancies) == 2
    assert vacancies[0].vacancy_id == '1'

    assert vacancies[1].vacancy_id == '2'
    assert vacancies[1].name == 'Java Developer'
    assert vacancies[1].url == 'https://hh.ru/vacancy/2'
    assert vacancies[1].employer == 'Corporation2'
    assert vacancies[1].requirement == 'Java skills'
    assert vacancies[1].responsibility == 'Develop Java applications'
    assert vacancies[1].salary_from == 150000
    assert vacancies[1].salary_to == 250000
    assert vacancies[1].currency == 'RUR'


def test_to_dict(vacancy_for_init):
    vacancy = Vacancy(**vacancy_for_init)
    vacancy_dict = vacancy.to_dict()

    assert vacancy_dict['vacancy_id'] == '1'
    assert vacancy_dict['name'] == 'Developer'
    assert vacancy_dict['url'] == 'https://hh.ru/vacancy/1'
    assert vacancy_dict['employer'] == 'Corporation'
    assert vacancy_dict['requirement'] == 'Python skills'
    assert vacancy_dict['responsibility'] == 'Develop Python applications'
    assert vacancy_dict['salary_from'] == 100000
    assert vacancy_dict['salary_to'] == 200000
    assert vacancy_dict['currency'] == 'RUR'
