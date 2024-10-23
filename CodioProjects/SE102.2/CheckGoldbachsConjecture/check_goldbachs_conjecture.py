# looks for all combinations of two primes that sum up to number.
def get_prime_summands(number):
    """
    :param number: int
    :return: list of tuples
    """
    prime_summands = []
    for first_summand in range(2, int(number/2)): # avoid printing reversed duplicates
        if not is_prime(first_summand):
            continue
        if is_prime(number - first_summand):
            prime_summands.append((first_summand, number - first_summand))
    return prime_summands


# Exception handling -> check if user provided the requested input.
def get_even_number_from_user():
    """
    :return: int
    """
    while True:
        try:
            user_input_number = int(input("Please enter a even number: "))
            if user_input_number % 2 == 0:
                return user_input_number
            print("Thats not an even number!")
        except:
            print("Thats not a number!")


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


def main():
    user_input_number = get_even_number_from_user()
    prime_summands = get_prime_summands(user_input_number)
    for summand1, summand2 in prime_summands:
        print(f"The number {user_input_number} equals to the sum of {summand1} and {summand2}")


if __name__ == "__main__":
    main()
