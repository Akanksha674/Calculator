try:
    a=int(input("Enter your first number :"))

    b=int(input("Enter your second number :"))

    print("What kind of operation do you want to perform.\nPress + for addition\npress - for subtraction\npress / for division\npress * for multiplication.")

    o=input("Enter operation: ")

    match o:
        case "+":
            print(f"The result is : {a + b} ")
        case "-":
            print(f"The result is : {a - b} ")
        case "/":
            print(f"The result is : {a / b} ")
        case "*":
            print(f"The result is : {a * b} ")
        case default:
            print("There was an error")
except Exception as e:
    print("Enter valid values of a and b")

