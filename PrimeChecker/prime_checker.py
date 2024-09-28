def is_prime(number):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


def primes_in_range(start, end):
    for i in list(range(start, end)):
        if is_prime(i):
            print(f"The number {i} is prime")


def main():
    print("Welcome to my PrimeChecker!")
    user_input_start = int(input("Please enter a positive number from which you want to start:"))
    user_input_end = int(input("Please enter a positive number where you want to end:"))
    primes_in_range(user_input_start, user_input_end)


if __name__ == "__main__":
    main()