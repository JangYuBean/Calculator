# add 함수 정의
def add(x, y):
    return x + y

def main():
    print("----------------------------")
    print("계산기 프로그램 입니다.")
    print("----------------------------")
    
    while True:
        print("\n사용할 기능을 선택하세요.")
        print("종료하려면 quit 입력하세요.")
        
        print("1. 더하기")
        print("2. 빼기")
        print("3. 곱하기")
        print("4. 나누기")
        
        choice = input("번호 : ")
        
        if choice == "quit":
            print("종료")
            break
        elif choice == "1":  # "1"번을 선택한 경우, add 함수 호출
            x = float(input("첫 번째 숫자 입력: "))
            y = float(input("두 번째 숫자 입력: "))
            print(f"결과: {add(x, y)}")  # add 함수 호출하여 결과 출력
        elif choice == "2":
            # 빼기 기능은 나중에 다른 브랜치에서 작업 예정
            pass
        elif choice == "3":
            # 곱하기 기능은 나중에 다른 브랜치에서 작업 예정
            pass
        elif choice == "4":
            # 나누기 기능은 나중에 다른 브랜치에서 작업 예정
            pass
        else:
            print("잘못된 입력.")

if __name__ == "__main__":
    main()
