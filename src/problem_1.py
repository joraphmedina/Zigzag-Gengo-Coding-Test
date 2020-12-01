import sys


def is_palindrome(input):
    """
    Simple palindrome checker
    """
    # If input is not string, we return False immediately
    if type(input) != str:
        return False

    # The specification says non-empty string, so we need to immediately return False for 0 length
    if len(input) == 0:
        return False

    # To reduce processing time, return True if length is 1
    if len(input) == 1:
        return True

    # Convert everything to lower case to allow checking.
    input = input.lower()

    # Remove whitespace characters to allow checking for phrases / palindromes with spaces
    input = input.replace(' ', '')

    # Reverse the string here
    reversed_string = "".join(reversed(input))

    # Check if both strings are equal
    return reversed_string == input


if __name__ == "__main__":
    string_inputs = sys.argv[1:]

    for item in string_inputs:
        print('Is {} a palindrome? {}'.format(item, is_palindrome(item)))
