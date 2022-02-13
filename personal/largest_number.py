first_number = int(input("Enter first number"))
second_number = int(input("Enter second number"))
third_number = int(input("Enter third number"))

def check_larget_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        largest_number = num1
    elif num2 > num3 and num2 > num1:
        largest_number = num2
    elif num3 > num1 and num3 > num2:
        largest_number = num3
    print(largest_number)

check_larget_number(first_number, second_number, third_number)
