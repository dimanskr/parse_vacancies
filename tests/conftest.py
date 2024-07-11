import pytest
from src.parser_classes import HH


@pytest.fixture
def hh():
    return HH(pages_count=3)
