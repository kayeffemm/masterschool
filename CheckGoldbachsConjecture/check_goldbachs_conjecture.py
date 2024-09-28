def get_prime_summands(number):
    prime_summands = []
    for first_summand in range(2, int(number/2)): # avoid printing reversed duplicates
        if not is_prime(first_summand):
            continue
        if is_prime(number - first_summand):
            prime_summands.append((first_summand, number - first_summand))
    return prime_summands


def get_even_number_from_user():
    while True:
        try:
            user_input_number = int(input("Please enter a even number: "))
            if user_input_number % 2 == 0:
                return user_input_number
            print("Thats not an even number!")
        except:
            print("Thats not a number!")


def is_prime(number):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


def main():
    user_input_number = get_even_number_from_user()
    prime_summands = get_prime_summands(user_input_number)
    for summand1, summand2 in prime_summands:
        print(f"The number {user_input_number} equals to the sum of {summand1} and {summand2}")


if __name__ == "__main__":
    main()