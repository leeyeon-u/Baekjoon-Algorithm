import sys

data = []
n = int(sys.stdin.readline())
for i in range(n):
    num_list = list(map(int,sys.stdin.readline().split()))
    break
find_num = int(input())
print(num_list.count(find_num))