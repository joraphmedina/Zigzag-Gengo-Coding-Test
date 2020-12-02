# Zigzag-Gengo-Coding-Test

### Submitted by: John Raphael Medina

### Setup
* Kindly create a python virtual environment by following the instructions [here](https://docs.python.org/3/library/venv.html)
* Activate the virtual environment by running `source <venv_path>/bin/activate`
* Install the needed libraries by running `pip install -r requirements.txt`

### Executing the unit tests
* To execute all unit tests, simply run the command `pytest` in the root folder
* To execute a single file, run `pytest tests/<name_of_file>.py`
* To execute a single function, run `pytest tests/<name_of_file>.py -k "<name_of_function>"`


### Executing the files
* To execute the files, simply run `python <filename> <system arguments>`
* * Note: Each script can take any number of arguments, enclose space-separated strings with quotation marks


### Solutions
**Problem 1**
* I simply wrote a function (`is_palindrome`) to check if the string is equal to its original once we get the reversed-order of the string
* To avoid unnecessary processing, it returns True immediately if length is 1.
* It can handle non-alphanumeric characters as well.
* For phrases, it will remove whitespaces to allow it to be recognized as a palindrome (similar to example "nurses run")
* Uses `O(2n)` space where `n` is the original string length
* Consumes `O(n)` time complexity as it iterates through the whole list


**Problem 2**
* Reused the `is_palindrome`
* To avoid unnecessary processing, if original string is already a palindrome, return the original string as the longest palindrome
* Start to process the string by iterating through substrings of length (original string length - 1)
* * We then create the possible substrings and check if there is a palindrome
* * If a palindrome is found, and it is already assumed that there is only 1, then we return that as the longest possible palindrome for the string input
* Uses at most `O(2n)` space where `n` is the original string length
* Consumes `O(n^2)` time complexity as it processes each substring combinations


**Problem 3**
* Reused the `is_palindrome` and `find_longest_palindrome` functions from Prolbem 1 and 2.
* To avoid unnecessary processing, if original string is already a palindrome, no need to partition so return 0.
* Given that we already have a way to find the longest possible palindrome, we make use of that by the following:
* * For a given string, find the longest possible palindrome
* * Once found, we split the original string into substrings by using the native `split()` function of python strings to acquire the non-palindromic substrings for each parts of the partitioned string
* * We do the same operation for each remaining substring
* * We get the sum of the number of substrings generated after each `split()` operation to correspond to our number of partitions.
* Consumes `O(n)` space due to the recursion
* However, the time complexity is at about `O(2^n)` also due to the recursive algorithm

### Other details
* The `reversed` function was used to check for Palindromes by checking if both strings are equal after the operation
* * Reversed() function is [found to be faster than splicing the array](https://www.geeksforgeeks.org/python-reversed-vs-1-which-one-is-faster/)
* Only the `main` branch was used throughout the development for the exam's purposes.
* python3.8 was used in the development of this exam
