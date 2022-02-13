def fibonacci(number):
    num1 = 0
    num2 = 1
    array = []

    for i in range(31):
        num3 = num1 + num2
        array.append(num3)
        num1 = num2
        num2 = num3
    print(array)
fibonacci(31)