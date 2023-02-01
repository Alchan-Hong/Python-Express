size = int(input("게임판의 크기: "))


for a in range(size):
    for i in range(size):
        print(" ---", end = " ")
    print("")
    for j in range(size+1):
        print("|   ", end = " ")
    print("")
for i in range(size):
        print(" ---", end = " ")



