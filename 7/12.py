
str = input("문자열을 입력하시오: ")
ban = input("금칙어를 입력하시오: ")

ban = ban.split(" ")


for i in range(len(ban)):
    if ban[i] in str:
        str = str.replace(ban[i], "*"*len(ban[i]))

print(str)

