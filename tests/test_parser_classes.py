def test_hh_init(hh):
    assert hh._url == 'https://api.hh.ru/vacancies'
    assert hh._headers == {'User-Agent': 'HH-User-Agent'}
    assert hh._params == {'text': '', 'page': 0, 'per_page': 100}
    assert hh._vacancies == []
    assert hh._pages_count == 3


def test_hh_vacancies_count(hh):
    vacancies = hh.load_vacancies("Python")
    assert len(vacancies) == 300
