def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide (a, b):
    return a / b

def exponent(base, exp):
    return base ** exp

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
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
