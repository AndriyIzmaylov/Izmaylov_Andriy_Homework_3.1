# Програма має виконувати прості математичні дії (+, -, *, /). Користувачеві пропонується по черзі ввести числа
# та дію над цими числами, а програма, виходячи з дії, обчислює та друкує результат.

# Зробити перевірку на те, що при діленні дільник не дорівнює 0!

from decimal import Decimal, InvalidOperation


def get_input_number(enter_phrase):
    while True:
        user_input_number = input(enter_phrase)
        try:
            return Decimal(user_input_number)
        except InvalidOperation:
            print("Error: Please, enter the correct number of Integer or Decimal")


def get_calculation_operator():
    while True:
        calculation_operator = input("Please, choose the calculation operation (+, -, *, /): ")
        if calculation_operator in ('+', '-', '*', '/'):
            return calculation_operator
        else:
            print("Error: Please, enter the right calculation operation!")


def calculate():
    print("***************** Simple Calculator *****************")

    first_entered_number = get_input_number("Please, enter the first number: ")

    chosen_calculation_operator = get_calculation_operator()

    if chosen_calculation_operator == '/':
        while True:
            second_entered_number = get_input_number("Please, enter the second number: ")
            if second_entered_number != 0:
                break
            print("Error: Cannot divide by zero!")
    else:
        second_entered_number = get_input_number("Please, enter the second number (the number should not be 0): ")

    if chosen_calculation_operator == '+':
        result = first_entered_number + second_entered_number
    elif chosen_calculation_operator == '-':
        result = first_entered_number - second_entered_number
    elif chosen_calculation_operator == '*':
        result = first_entered_number * second_entered_number
    elif chosen_calculation_operator == '/':
        result = first_entered_number / second_entered_number

    print(f"Result: {result}")


calculate()
