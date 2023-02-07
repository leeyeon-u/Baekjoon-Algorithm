import sys

M, N = list(map(int, sys.stdin.readline().split()))

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i, end="\n")


'''Continue와 Pass 차이
# Continue: 하위 코딩을 건너뛰고 다음 순번의 loop를 수행
# Pass: 실행할 코드가 없는 것으로 다음 행동을 수행
'''


