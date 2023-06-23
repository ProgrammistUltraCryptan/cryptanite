def calculator():
    print("Simple Calculator")
    print("Enter 'q' to quit")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed")
                    continue
                result = num1 / num2
            else:
                print("Error: Invalid operator")
                continue

            print("Result:", result)

        except ValueError:
            print("Error: Invalid input")
        except KeyboardInterrupt:
            print("\nCalculator stopped")
            break


calculator()
