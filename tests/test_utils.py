from src.utils import currency_to_rub_coefficient


def test_currency_to_rub_coefficient():
    # Проверка для валюты, которая есть в словаре
    assert currency_to_rub_coefficient('USD') == 88.85
    assert currency_to_rub_coefficient('EUR') == 96.1783

    # Проверка для валюты, которая отсутствует в словаре (должен вернуться коэффициент по умолчанию, равный 1)
    assert currency_to_rub_coefficient('JPY') == 1


def test_currency_to_rub_coefficient_with_no_value():
    # Проверка поведения функции при некорректных данных (например, None)
    assert currency_to_rub_coefficient(None) == 1

