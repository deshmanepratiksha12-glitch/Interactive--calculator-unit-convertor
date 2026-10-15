def calculator():
    while True:
        print("\n--- CALCULATOR & UNIT CONVERTER ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Kilometers to Miles")
        print("6. Celsius to Fahrenheit")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Thank you!")
            break

        elif choice in ["5", "6"]:
            try:
                value = float(input("Enter value: "))

                if choice == "5":
                    print("Miles =", value * 0.621371)
                else:
                    print("Fahrenheit =", (value * 9 / 5) + 32)

            except ValueError:
                print("Invalid input! Enter a number.")

        elif choice in ["1", "2", "3", "4"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    print("Result =", a + b)
                elif choice == "2":
                    print("Result =", a - b)
                elif choice == "3":
                    print("Result =", a * b)
                elif choice == "4":
                    if b != 0:
                        print("Result =", a / b)
                    else:
                        print("Cannot divide by zero!")

            except ValueError:
                print("Invalid input! Enter numbers only.")

        else:
            print("Invalid choice! Please try again.")


calculator()
