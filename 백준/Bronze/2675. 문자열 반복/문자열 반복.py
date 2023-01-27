import sys

num = int(input())
P = ""
for i in range(num):
    S, R = sys.stdin.readline().split()
    for j in R:
        print(j*int(S), end="")
    print()