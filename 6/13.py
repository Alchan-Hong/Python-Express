
print("-----------------------")
print("  1 2 3 4 5 6 7 8 9 10")
print("-----------------------")

seats = []
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

for row in seats:
    print(row)
print("")

def reserve():
    row = int(input("원하시는 자석의 행번호를 입력하세요(종료는 -1): "))
    column = int(input("원하시는 자석의 열번호를 입력하세요(종료는 -1): "))
    
    if seats[row][column] == 1:
        print("예약할 수 없습니다.")
    elif seats[row][column] == -1:
        print("종료")
    else:
        print("예약되었습니다.")
        seats[row][column] = 1

reserve()








