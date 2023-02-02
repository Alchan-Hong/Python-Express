str1 = input("첫 번째 문자열: ")
str2 = input("두 번째 문자열: ")

common = []

common = [set(str1) & set(str2)]

print("모두 포함된 글자: ", common)

