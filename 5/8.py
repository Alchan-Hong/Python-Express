
def getMoneyText(amount):
    chStr = "영일이삼사오육칠팔구"

    return chStr[amount]

Don = "천백십원"
money = input("1000 이하의 금액을 입력하시오: ")

if len(money) == 3:
    money = "0" + money
elif len(money) == 2:
    money = "00" + money
elif len(money) == 1:
    money = "000" + money

Str = ""

for i in range(len(money)):
    if money[i] != "0":
        Str += getMoneyText(int(money[i])) + Don[i] + ""
if money[len(money)-1] == "0":
    Str += "원"

print(Str)
