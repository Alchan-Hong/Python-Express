
Mystr = input("")

word = sum(1 for x in Mystr if x.isalpha())
number = sum(1 for y in Mystr if y.isnumeric())

print(Mystr, "-> " "LETTERS :", word, "DIGITS :", number)


