
while True:
    date = input("날짜를 MM/DD/YYYY 형식으로 입력하시오.")
    if date == "0":
        break
    d = date.split("/")
    sor = [ d[2], d[0], d[1] ]
    date = "".join(sor)
    print("->", date)
    

