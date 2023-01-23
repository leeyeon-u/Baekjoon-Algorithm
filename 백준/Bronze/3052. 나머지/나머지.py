
list_a = []
list_b = []

for i in range(10):
    list_a.append(int(input()))
    list_b.append(list_a[i]%42)

print(len(set(list_b)))
