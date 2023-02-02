
set1 = {10, 20, 30, 40, 50, 60}
set2 = {30, 40, 50, 60, 70, 80}

print("첫 번째 세트", sorted(set1))
print("두 번째 세트", sorted(set2))

total = set1|set2
gyojiphap = set1 & set2 #교집합

result = total.difference(gyojiphap)

print("어느 한 쪽에만 있는 요소들", sorted(result))

