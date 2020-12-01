import pytest

from src.problem_2 import find_longest_palindrome


# Valid cases
def test_valid_single_character():
    """
    Single-character strings are palindromes by default
    """
    assert find_longest_palindrome('a') == 'a'


def test_valid_numerical_string():
    """
    Test for numerical string palindromes
    """
    assert find_longest_palindrome('12321') == '12321'


def test_valid_string_basic_case():
    """
    Simple test case for a single-word string
    """
    assert find_longest_palindrome('eye') == 'eye'


def test_valid_string_basic_case():
    """
    Simple test case for a single-word string in all capital letters
    """
    assert find_longest_palindrome('EYE') == 'eye'


def test_valid_string_camel_case():
    """
    Simple test case for camel-cased strings
    """
    assert find_longest_palindrome('RaCeCar') == 'racecar'


def test_valid_phrase():
    """
    Test case for phrases with white spaces
    """
    assert find_longest_palindrome("nurses run") == 'nursesrun'


def test_valid_input_with_symbols():
    """
    Test case for phrases with special characters
    """
    assert find_longest_palindrome("a!!a") == 'a!!a'


def test_valid_input_with_symbols_and_spaces():
    """
    Test case for phrases with special characters and white spaces
    """
    assert find_longest_palindrome("a! !a") == 'a!!a'


def test_valid_substring_palindrome():
    """
    Test for string with a substring as the longest palindrome
    """
    assert find_longest_palindrome('abaxyzzyxf') == 'xyzzyx'


def test_valid_substring_palindrome_case2():
    """
    Test for string with a substring as the longest palindrome with camel-case string
    """
    assert find_longest_palindrome('abaXyZzYxF') == 'xyzzyx'


def test_valid_substring_phrase_palindrome():
    """
    Test for string with a substring as the longest palindrome
    """
    assert find_longest_palindrome('Why do nurses run in hospitals') == 'nursesrun'


def test_valid_multiple_palindromes():
    """
    Test for substring with multiple palindromes inside the string
    """
    assert find_longest_palindrome('zaaaybcccb') == 'bcccb'


def test_valid_multiple_palindromes_case2():
    """
    Test for substring with multiple palindromes inside the string
    """
    assert find_longest_palindrome('zaaaybcccbabcdddddddddddddddddd') == 'dddddddddddddddddd'
