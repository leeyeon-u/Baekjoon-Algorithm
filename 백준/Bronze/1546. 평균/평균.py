import sys

A = int(input())
list_a = list(map(int, sys.stdin.readline().split()))
list_b = []

for i in range(A):
    M = max(list_a)
    list_b.append(list_a[i]/M*100)

print(sum(list_b)/A)






