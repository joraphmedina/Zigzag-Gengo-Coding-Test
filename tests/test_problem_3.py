import pytest

from src.problem_3 import find_palindrome_partitions


# Valid cases
def test_valid_single_character():
    """
    Single-character strings are palindromes by default
    """
    assert find_palindrome_partitions('a') == 0


def test_valid_numerical_string():
    """
    Test for numerical string palindromes
    """
    assert find_palindrome_partitions('12321') == 0


def test_valid_string_basic_case():
    """
    Simple test case for a single-word string
    """
    assert find_palindrome_partitions('eye') == 0


def test_valid_string_basic_case():
    """
    Simple test case for a single-word string in all capital letters
    """
    assert find_palindrome_partitions('EYE') == 0


def test_valid_string_camel_case():
    """
    Simple test case for camel-cased strings
    """
    assert find_palindrome_partitions('RaCeCar') == 0


def test_valid_phrase():
    """
    Test case for phrases with white spaces
    """
    assert find_palindrome_partitions("nurses run") == 0


def test_valid_input_with_symbols():
    """
    Test case for phrases with special characters
    """
    assert find_palindrome_partitions("a!!a") == 0


def test_valid_input_with_symbols_and_spaces():
    """
    Test case for phrases with special characters and white spaces
    """
    assert find_palindrome_partitions("a! !a") == 0


def test_valid_substring_palindrome_one():
    """
    Test for string with a substring as the longest palindrome
    """
    assert find_palindrome_partitions('beye') == 1


def test_valid_substring_palindrome_example():
    """
    Test for string with a substring as the longest palindrome
    """
    assert find_palindrome_partitions('noonabbad') == 2


def test_valid_substring_palindrome():
    """
    Test for string with a substring as the longest palindrome
    """
    assert find_palindrome_partitions('abaxyzzyxf') == 2


def test_valid_substring_palindrome_case2():
    """
    Test for string with a substring as the longest palindrome with camel-case string
    """
    assert find_palindrome_partitions('abaXyZzYxF') == 2


def test_valid_substring_phrase_palindrome():
    """
    Test for string with a substring as the longest palindrome
    """
    assert find_palindrome_partitions('Why do nurses run in hospitals') == 16


def test_valid_multiple_palindromes():
    """
    Test for substring with multiple palindromes inside the string
    """
    assert find_palindrome_partitions('zaaaybcccb') == 3


def test_valid_multiple_palindromes_case2():
    """
    Test for substring with multiple palindromes inside the string
    """
    assert find_palindrome_partitions('zaaaybcccbabcdddddddddddddddddd') == 7
