import random

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
passlen = 8

password = "".join(random.sample(s, passlen))

print("생성된 암호 = ", password)

