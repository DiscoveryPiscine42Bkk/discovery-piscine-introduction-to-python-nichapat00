#!/usr/bin/env python3

def main():
    print("Enter a number less than 25")
    try:
        num = int(input())
        if num > 25:
            print("Error")
        else:
            while num <= 25:
                print(f"Inside the loop, my variable is {num}")
                num += 1
    except ValueError:
        print("Invalid input. Please enter a number.")
