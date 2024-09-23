# 1 = 1
# 2 = 2
# 3 = "Fizz"
# 4 = 4
# 5 = "Buzz"
# 6 = "Fizz"
# 7 = "Lazz"
# 10 = "Buzz"
# 15 = "FizzBuzz"
# 21 = "FizzLazz"
# 35 = "BuzzLazz"
# 105 = "FizzBuzzLazz"

def checker(number_list):
    fizzbuzz_list = []
    for i in number_list:
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if i % 7 == 0:
            s += "Lazz"
        if s == "":
                s = str(i)
        fizzbuzz_list.append(s)
    print(fizzbuzz_list)

checker(list(range(1, 360)))