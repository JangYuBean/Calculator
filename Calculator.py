def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
feature/divide
def divide (a, b):
    return a / b
def main():
    print("----------------------------")
    print("계산기 프로그램 입니다.")
    print("----------------------------")
    while True:
        print("\n사용할 기능을 선택하세요. 종료하려면 'quit'를 입력하세요.")
        print("1. 더하기")
        print("2. 빼기")

        choice = input("번호 : ")

        if choice == "quit":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            x = float(input("첫 번째 숫자 입력: "))
            y = float(input("두 번째 숫자 입력: "))
            print(f"결과: {x} + {y} = {x + y}")
        elif choice == "2":
            x = float(input("첫 번째 숫자 입력: "))
            y = float(input("두 번째 숫자 입력: "))
            print(f"결과: {x} - {y} = {subtract(x, y)}")

        elif choice == "3":
            x = float(input("첫 번째 숫자 입력: "))
            y = float(input("두 번째 숫자 입력: "))
            print(f"결과: {x} - {y} = {multiply(x, y)}")
feature/divide
        elif choice == "4":
            x = float(input("첫 번째 숫자 입력: "))
            y = float(input("두 번째 숫자 입력: "))
            if y != 0:
                print(f"결과: {x} / {y} = {divide(x, y)}")
            else:
                print("0으로 나눌 수 없습니다.")
        

main

def multiply(a, b):
    return a * b

def divide (a, b):
    return a / b

def exponent(base, exp):
    return base ** exp

def sqrt(number):
    if number < 0:
        return "음수의 제곱근은 정의되지 않습니다."
    return math.sqrt(number)
def main():
    print("----------------------------")
    print("계산기 프로그램 입니다.")
    print("----------------------------")
    while True:
        print("\n사용할 기능을 선택하세요. 종료하려면 'quit'를 입력하세요.")
        print("1. 더하기")
        print("2. 빼기")
        print("3. 곱하기")
        print("4. 나누기")
        print("5. 지수 계산 (x^y)")
        print("6. 제곱근 계산 (√x)")


        choice = input("번호 : ")

        if choice == "quit":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            x = float(input("첫 번째 숫자 입력: "))
            y = float(input("두 번째 숫자 입력: "))
            print(f"결과: {x} + {y} = {x + y}")
        elif choice == "2":
            x = float(input("첫 번째 숫자 입력: "))
            y = float(input("두 번째 숫자 입력: "))
            print(f"결과: {x} - {y} = {subtract(x, y)}")
        elif choice == "3":
            x = float(input("첫 번째 숫자 입력: "))
            y = float(input("두 번째 숫자 입력: "))
            print(f"결과: {x} - {y} = {multiply(x, y)}")
        elif choice == "4":
            x = float(input("첫 번째 숫자 입력: "))
            y = float(input("두 번째 숫자 입력: "))
            if y != 0:
                print(f"결과: {x} / {y} = {divide(x, y)}")
        elif choice == "5":
            base = float(input("밑(base) 값을 입력하세요: "))
            exp = float(input("지수(exponent) 값을 입력하세요: "))
            print(f"결과: {base}^{exp} = {exponent(base, exp)}")
        elif choice == "6":
            number = float(input("숫자를 입력하세요: "))
            print(f"결과: √{number} = {sqrt(number)}")
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
else:
    print("잘못된 입력입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()

main
