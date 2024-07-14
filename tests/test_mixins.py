from src.mixins import CleanTagsMixin


def test_clean_tags():
    assert CleanTagsMixin.clean_tags('<tag>Text1</tag>') == 'Text1'
    assert CleanTagsMixin.clean_tags('<tag1>Some</tag1><tag2> text</tag2>') == 'Some text'
    assert CleanTagsMixin.clean_tags('No tags') == 'No tags'
    assert CleanTagsMixin.clean_tags('') == ''


def test_clean_tags_with_empty_input():
    assert CleanTagsMixin.clean_tags(None) is None
