def letter_count(string):
    """Returns the number of letters within a string before normalize it.

    To be pricise in the number of letters within the string the input must be set to lower case and
    it's spaces removed."""
    letters_dict = {}
    normalized_string = string.lower().replace(' ', '')
    for letter in set(normalized_string):
        letters_dict[letter] = normalized_string.count(letter)

    return(letters_dict)

# To test this program with a user input please uncomment the following lines
# string = raw_input("Give me a string: ")
# print(letter_count(string))
