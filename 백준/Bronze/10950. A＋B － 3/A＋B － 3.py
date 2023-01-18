test_case = int(input())
cnt = 0
while True:
    A, B = list(map(int,input().split()))
    print(A+B)
    cnt += 1
    if cnt == test_case:
        break