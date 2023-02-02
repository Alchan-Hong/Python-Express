def found():
    if key in dict:
        print(f"키 {key}은 딕셔너리에 있습니다.")
    else:
        print("키는 딕셔너리에 없습니다.")


dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key = int(input("키를 입력하시오: "))

found()
