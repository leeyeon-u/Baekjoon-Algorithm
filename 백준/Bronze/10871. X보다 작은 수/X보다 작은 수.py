import sys

N, X = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    if num_list[i] < X:
        print(num_list[i], end=" ")