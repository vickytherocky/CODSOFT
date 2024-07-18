while True:
    operation = input("Enter the operation (+, -, *, /): ")
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    
    if operation == "+":
        result = first_number + second_number
        print(f"{first_number} + {second_number} = {result}")
    elif operation == "-":
        result = first_number - second_number
        print(f"{first_number} - {second_number} = {result}")
    elif operation == "*":
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")
    elif operation == "/":
        if second_number == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result}")
    else:
        print("Invalid operation symbol. Please use +, -, *, or /.")
    
    choice = input("Do you want to quit? (y/n): ")
    if choice.lower() == 'y':
        break

print("Thank you for using the calculator!")
