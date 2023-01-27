hansoo = 0
N = int(input())
for i in range(1, N+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        hansoo += 1
    elif num_list[0]-num_list[1] == num_list[1] - num_list[2]:
        hansoo += 1

print(hansoo)
