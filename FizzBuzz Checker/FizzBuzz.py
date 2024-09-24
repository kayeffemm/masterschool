# 3 = Fizz
# 5 = Buzz
# 7 = Lazz
# 3 & 5 = FizzBuzz
# 3 & 7 = FizzLazz
# 5 & 7 = BuzzLazz
# 3 & 5 & 7 = FizzBuzzLazz

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