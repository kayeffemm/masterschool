def calculate(text_input):
    calculation, seperator = split_user_input(text_input)
    num1 = int(calculation[0])
    num2 = int(calculation[1])
    if seperator == "+":
        return f"The answer is {num1 + num2}"
    elif seperator == "-":
        return f"The answer is {num1 - num2}"
    elif seperator == "*":
        return f"The answer is {num1 * num2}"
    elif seperator == "/":
        return f"The answer is {num1 / num2}"
    elif seperator == "~":
        return f"The answer is {num1 // num2}\nThe remainder is {num1 % num2}"

def split_user_input(calculation):
    calculation_lst = []
    seperator = ""
    if "+" in calculation:
        seperator += "+"
        calculation_lst = calculation.split("+")
    elif "-" in calculation:
        seperator += "-"
        calculation_lst = calculation.split("-")
    elif "*" in calculation:
        seperator += "*"
        calculation_lst = calculation.split("*")
    elif "/" in calculation:
        seperator += "/"
        calculation_lst = calculation.split("/")
    elif "~" in calculation:
        seperator += "~"
        calculation_lst = calculation.split("~")

    return calculation_lst, seperator

def calc_iterations(iterations):
     for _ in range(int(iterations)):
        user_input = input("What do you want to calculate? ")
        print(calculate(user_input))

print("Welcome to the Python calculator!")
user_input = input("How many calculation do you want to do?")
calc_iterations(user_input)