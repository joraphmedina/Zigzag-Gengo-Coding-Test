import pytest

from src.problem_1 import is_palindrome


# Invalid cases
def test_invalid_zero_length_string():
    """
    The specifications say that non-empty string, so empty strings are invalid
    """
    assert is_palindrome('') is False


def test_invalid_integer_input():
    """
    Test for non-string input
    """
    assert is_palindrome(1) is False


def test_invalid_float_input():
    """
    Test for non-string input
    """
    assert is_palindrome(1.00) is False


def test_invalid_character_input():
    """
    Test for invalid string
    """
    assert is_palindrome('string') is False


def test_invalid_character_phrase_input():
    """
    Test for invalid string
    """
    assert is_palindrome('string input') is False


def test_invalid_numerical_string():
    """
    Test for invalid numerical string
    """
    assert is_palindrome('12345') is False


def test_invalid_special_string():
    """
    Test for invalid numerical string
    """
    assert is_palindrome('!@#$%') is False


# Valid cases
def test_valid_single_character():
    """
    Single-character strings are palindromes by default
    """
    assert is_palindrome('a') is True


def test_valid_numerical_string():
    """
    Single-character strings are palindromes by default
    """
    assert is_palindrome('12321') is True


def test_valid_string_basic_case():
    """
    Simple test case for a single-word string
    """
    assert is_palindrome('eye') is True


def test_valid_string_basic_case():
    """
    Simple test case for a single-word string in all capital letters
    """
    assert is_palindrome('EYE') is True


def test_valid_string_camel_case():
    """
    Simple test case for camel-cased strings
    """
    assert is_palindrome('RaCeCar') is True


def test_valid_phrase():
    """
    Test case for phrases with white spaces
    """
    assert is_palindrome("nurses run") is True


def test_valid_input_with_symbols():
    """
    Test case for phrases with special characters
    """
    assert is_palindrome("a!!a") is True


def test_valid_input_with_symbols_and_spaces():
    """
    Test case for phrases with special characters and white spaces
    """
    assert is_palindrome("a! !a") is True
