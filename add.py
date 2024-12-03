# calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The addition result is: {add(num1, num2)}")
