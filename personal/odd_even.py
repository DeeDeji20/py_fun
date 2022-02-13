number = int(input("Enter a number: "))

def check_that_number_is_odd_or_even(user_input):
    if user_input % 2 == 0: return True
    else: return False
print(check_that_number_is_odd_or_even(number))
