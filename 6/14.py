import random

bomb = [['.'for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        R = random.random()
        if R <= 0.3:
            bomb[i][j] = '#'
        print(bomb[i][j], end = " ")
    print()


