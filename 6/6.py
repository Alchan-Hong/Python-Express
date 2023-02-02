
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10]

common = [i for i in list1 if i in list2]

if common != []:
    print("True")







list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10]

def common(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

def common2(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

print(common(list1, list2))
print(common2(list1, list2))
