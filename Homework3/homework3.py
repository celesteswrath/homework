while True:
    a = int(input("Enter 'a' value: "))
    b = int(input("Enter 'b' value: "))
    try:
        c = a / b
        print(c)
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    print("Out of try except blocks")
