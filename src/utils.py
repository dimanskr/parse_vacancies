from settings import CURRENCY_MATCH_RUB


def currency_to_rub_coefficient(currency: str | None) -> float:
    """
    Преобразование других валют в рубли. Данные курса валют берутся из словаря, но в идеале должны браться с API биржи
    :param currency: str
    :return: float RUB/OTHER_CURRENCY
    """
    return CURRENCY_MATCH_RUB.get(currency, 1)



