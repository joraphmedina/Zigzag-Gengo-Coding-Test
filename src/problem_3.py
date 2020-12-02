import sys

from src.problem_1 import is_palindrome
from src.problem_2 import find_longest_palindrome


def find_palindrome_partitions(input):
    """
    Function to get minimum number of cuts on the input
    such that each remaining substring is a palindrome
    """

    # If whole string is a palindrome, no need to cut
    if is_palindrome(input):
        return 0

    # Remove whitespaces for easier processing
    input = input.replace(' ', '')
    # Make sure all characters are lower case
    input = input.lower()

    return check_partitions(input)


def check_partitions(input):
    """
    Get and determine the number of partitions needed to achive that
    every substring is a palindrome
    """

    """
    No need to partition if length is already 1
    """
    if len(input) == 1:
        return 0
    current_split_count = 0
    longest_palindrome = find_longest_palindrome(input)

    if longest_palindrome == '':
        """
        If there are no more palindromic strings,
        we divide them into single-character strings to make them palindromic
        We do not need to split the last character so we get (length - 1)
        """
        return len(input) - 1
    else:
        """
        We split the string according to the longest palindrome found
        The number of splits would be the number of substrings after the split
        """
        substrings = input.split(longest_palindrome)
        current_split_count += len(substrings)
        for item in substrings:
            """
            We execute this function recurisvely for each remaining substring
            """
            current_split_count += check_partitions(item)

    return current_split_count
