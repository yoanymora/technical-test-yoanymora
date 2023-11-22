import math

def is_palindrome(string):
    """Indicates if a string is a palindrome or not

    First modify the string into a list to make it easy to sort, then split the list into two smaller lists
    this helps to compare the first half of the list vs the last half of the list reversed.

    Params:
        string (str): String to check if it's or not a palindrome
    Returns:
        string indicating if the input is a palindrome"""
    if not string:
        return "Please enter a valid string."
    string_list = list(string)
    is_palindrome = False
    first_half_index = int(math.floor(float(len(string_list)) / 2) if float(len(string_list)) % 2 != 0 else float(len(string_list)) / 2)
    last_half_index = int(math.ceil(float(len(string_list)) / 2) if float(len(string_list)) % 2 != 0 else float(len(string_list)) / 2)
    first_half, last_half = string_list[:first_half_index], string_list[last_half_index:]
    last_half.sort(reverse=True)
    is_palindrome = first_half == last_half

    return "The string %s %s a palindrome." % (string, "is" if is_palindrome else "isn't")

# To run this program with a user input please uncomment those lines
# string = raw_input("Give me a string: ")
# print(is_palindrome(string))