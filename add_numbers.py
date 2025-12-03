#!/usr/bin/env python3
"""
Simple script to read two numbers from console and display their sum.
"""

def main():
    # Read first number
    num1 = float(input("Enter the first number: "))

    # Read second number
    num2 = float(input("Enter the second number: "))

    # Calculate sum
    result = num1 + num2

    # Display result
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
