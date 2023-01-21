import sys

N = int(input())
for i in range(N):
    num_list = list(map(int, sys.stdin.readline().split()))
    break
print(min(num_list), max(num_list))
