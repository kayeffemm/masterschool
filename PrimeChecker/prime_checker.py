# checks if number is prime.
def is_prime(number):
    """
    :param number: int
    :return: bool
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    limit = int(number ** 0.5)
    for i in range(5, limit + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True


# prints all primes in given range.
def primes_in_range(start, end):
    """
    :param start: int
    :param end: int
    :return: bool
    """
    for i in list(range(start, end)):
        if is_prime(i):
            print(f"The number {i} is prime")


# prompts the user to enter a positive, whole number and calls the primes_in_range function to print out the primes.
def main():
    print("Welcome to my PrimeChecker!")
    while True:
        try:
            user_input_start = int(input("Please enter a positive number from which you want to start: "))
            user_input_end = int(input("Please enter a positive number where you want to end: "))
            primes_in_range(user_input_start, user_input_end)
            break
        except ValueError as e:
            print("Please only enter positive whole numbers! Error:", e)


if __name__ == "__main__":
    main()
