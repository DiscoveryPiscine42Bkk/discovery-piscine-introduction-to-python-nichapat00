#!/usr/bin/env python3

def main():
    try:
        print("Enter the first number:")
        num1 = int(input())
        print("Enter the second number:")
        num2 = int(input())

        result = num1 * num2
        print(f"{num1} x {num2} = {result}")

        if result > 0:
            print("The result is positive.")
        elif result < 0:
            print("The result is negative.")
        else:
            print("The result is positive and negative.")
    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
