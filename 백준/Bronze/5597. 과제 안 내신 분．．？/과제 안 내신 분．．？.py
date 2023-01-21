import sys

list_a = []
list_b = []
for i in range(1, 31):
    list_a.append(i)

for i in range(28):
    list_b.append(int(input()))

assignment = list(set(list_a) - set(list_b))
print(min(assignment))
print(max(assignment))
