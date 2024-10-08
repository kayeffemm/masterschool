def get_grade(subject: str) -> float:
    """
    prompts user to input a valid grade for the given subject and returns it as a float.
    :param subject: str
    :return: float
    """
    while True:
        try:
            user_input_grade = float(input(f"Please enter {subject} grade: "))
            if 0 <= user_input_grade <= 100:
                return user_input_grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Expected a number, please try again.")


def get_student_info() -> dict:
    """
    prompts the user to provide student information.
    :return: dict
    """
    user_input_student_name = input("Enter name: ")
    user_input_math_grade = get_grade("Math")
    user_input_english_grade = get_grade("English")
    student_info_dictionary = {"Name": user_input_student_name,
                               "English": user_input_english_grade,
                               "Math": user_input_math_grade
                               }
    return student_info_dictionary


def get_student_amount() -> int:
    """
    prompts user to input the amount of students, checks if its an positive integer and returns it.
    :return: int
    """
    while True:
        try:
            user_input_number_of_students = int(input("Please enter the number of students: "))
            if user_input_number_of_students > 0:
                return user_input_number_of_students
            else:
                print("Please enter a positive number of students.")
        except ValueError:
            print("Expected a number, please try again.")


def print_student_info(students: list):
    """
    takes a list of dictionaries containing student information and prints their name, best grade and average grade.
    :param students: list of dictionaries
    :return: None
    """
    for student in students:
        student_name = student["Name"]
        best_grade = 0
        average_grade = (student["English"] + student["Math"]) / 2
        if student["English"] > student["Math"]:
            best_grade += student["English"]
        else:
            best_grade += student["Math"]
        print(f"Student: {student_name}, Best Grade: {best_grade}, Average Grade: {average_grade}")


def calculate_average_grades(students: list) -> tuple:
    """
    calculates the average grade of a subject and the overall average grade across all subject and returns a tuple
    :param students: list
    :return: tuple
    """
    sum_of_math_grades = 0
    sum_of_english_grades = 0
    for i in range(len(students)):
        sum_of_math_grades += students[i]["Math"]
        sum_of_english_grades += students[i]["English"]

    average_of_math_grades = sum_of_math_grades / len(students)
    average_of_english_grades = sum_of_english_grades / len(students)
    average_grade_per_subject = {"Math": average_of_math_grades, "English": average_of_english_grades}

    overall_average_grade = (average_of_math_grades + average_of_english_grades) / 2

    return average_grade_per_subject, overall_average_grade


def calculate_failing_grades(students: list) -> dict:
    """
    iterates over the students list and returns a dictionary containing students name and the sum of failed grades
    :param students: list of dicts
    :return: dict
    """
    students_failing_dictionary = {}
    for i in range(len(students)):
        current_student_name = students[i]["Name"]
        students_failing_dictionary[current_student_name] = 0
        if students[i]["Math"] <= 55:
            students_failing_dictionary[current_student_name] += 1
        if students[i]["English"] <= 55:
            students_failing_dictionary[current_student_name] += 1
    return students_failing_dictionary


def main():
    student_amount = get_student_amount()
    student_list = []
    for _ in range(student_amount):
        print(f"Enter details for student {_ + 1}:")
        student_info = get_student_info()
        print()
        student_list.append(student_info)
    print_student_info(student_list)
    average_grade_per_subject, overall_average_grade = calculate_average_grades(student_list)
    print("\nAverage grades per subject:")
    for subject, average_grade in average_grade_per_subject.items():
        print(f"{subject}: {average_grade}")

    print(f"\nOverall average grade across all subjects: {overall_average_grade}")

    print("\nFailing grades per student:")
    students_failing_dictionary = calculate_failing_grades(student_list)
    sum_of_failing_grades_across_all_students = 0
    for name, failing_grades_amount in students_failing_dictionary.items():
        sum_of_failing_grades_across_all_students += students_failing_dictionary[name]
        print(f"{name}: {failing_grades_amount} failing grade(s)")
    print(f"\nTotal number of failing grades across all students: {sum_of_failing_grades_across_all_students}")


if __name__ == "__main__":
    main()
