import sys

from src.problem_1 import is_palindrome


def find_longest_palindrome(input):
    """
    Function to get longest palindromic substring of given input
    It is stated that a valid string is already given.
    """

    # Check if input is already a palindrome itself
    # If yes, we just return the input
    if is_palindrome(input):
        input = input.replace(' ', '')
        return input.lower()

    # Do the processing here
    longest_palindrome = find_palindromes(input)

    return longest_palindrome


def find_palindromes(input):
    """
    Function to find the palindromes if input is not a palindrome itself
    We start by getting substrings of length N where N <= (max_length - 1)
    Once a palindrome is found,
    We return the function as it is supposed to be the longest palindrome
    """
    # Get substrings of the input and check using the palindrome
    max_index = 1
    # Starts at (length - 1)
    max_palindrome_length = len(input) - max_index
    longest_palindrome = ''

    while max_palindrome_length > 1:
        start_index = 0
        end_index = max_palindrome_length

        while start_index <= max_index:
            # Generate substrings of Length N here
            # Where N is the current value of the max_palindrome_length
            substr_input = input[start_index:end_index]

            if is_palindrome(substr_input) is True and \
                    len(longest_palindrome) < len(substr_input):
                # Once a palindrome is found, we return the function
                substr_input = substr_input.replace(' ', '')
                return substr_input.lower()

            start_index += 1
            end_index += 1

        max_palindrome_length -= 1
        max_index += 1

    return longest_palindrome


if __name__ == "__main__":
    string_inputs = sys.argv[1:]

    for item in string_inputs:
        print('Longest palindrome for input {} is: {}'.format(item, find_longest_palindrome(item)))
