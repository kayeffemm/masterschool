def is_divisible_by(number, by):
    return number % by == 0


def is_prime(number):
    range_halved = int(number/2)
    for i in range(range_halved):
        if i > 1:
            if is_divisible_by(number, i):
                return False
    if number <= 1:
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