def is_prime_number(number):
    """Indicate if a number is, or not, a prime number.

    To solve this problem I'm using the Divisibility Tests to find the number of factors of the input,
    if this is bigger than 2 the input isn't prime.

    Params:
        number (int): Value to check if it's, or not, a prime number.
    Returns:
        string indicating if the input is a prime number"""

    if number <= 0:
        return "Please input a number bigger than 0"

    is_prime = False
    if number > 0 and number <= 10:
        factors = 0
        for N in range(1, 10):
            if N <= number and number % N == 0:
                factors += 1

    if number >= 10:
        factors = 2
        if str(number)[-1] != '0' and str(number)[-1] != '5':
            if number % 2 == 0 or number % 3 == 0 or number % 9 == 0:
                factors += 1
        else:
            factors += 1

    is_prime = factors == 2

    return "The number %s %s prime." % (number, "is" if is_prime else "isn't")

# To test this program with a user input please uncomment the following lines
# number = input("Give me a number: ")
# print(is_prime_number(number))
