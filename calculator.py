def calculator():
    print("Welcome to the Simple Calculator!")
    
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Enter the number corresponding to the operation (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid operation.")
            continue

        try:
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            result = n1 + n2
            operation = '+'
        elif choice == '2':
            result = n1 - n2
            operation = '-'
        elif choice == '3':
            result = n1 * n2
            operation = '*'
        elif choice == '4':
            if n2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = n1 / n2
            operation = '/'

        print(f"The result of {n1} {operation} {n2} is: {result}")

if __name__ == "__main__":
    calculator()
