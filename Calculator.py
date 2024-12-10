def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

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
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
