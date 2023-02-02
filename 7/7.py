

calender = {}

for i in range(2):
    day = input("날짜를 입력하시오: ")
    plan = input("일정을 입력하시오: ")

    if day in calender:
        calender[day].append(plan)
    else:
        calender[day] = []
        calender[day].append(plan)


print(calender)


