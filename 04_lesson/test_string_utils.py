import pytest

from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("всем привет!", "Всем привет!"), ("hello people", "Hello people")])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"), ("", ""), ("   ", "   ")])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    (" Вперёд!", "Вперёд!"), ("         hello people", "hello people")])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("Charge!", "Charge!"), ("12 стульев", "12 стульев"), ("", "")])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("string, symbol", [
    ("Volga", "V"), ("Сыр", "ы"), ("Доброе утро!", "!")])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol)


@pytest.mark.parametrize("string, symbol", [
    ("Доброе утро!", "а"), ("/", " "), (" ", "123 ")])
def test_contains_negative(string, symbol):
    assert string_utils.contains(string, symbol) is False


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "kyP", "Sro"), ("ошибка", "ш", "оибка"), ("12367", "236", "17")])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("Sky", "P", "Sky"), ("", "a", ""), ("abc", "d", "abc")])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
