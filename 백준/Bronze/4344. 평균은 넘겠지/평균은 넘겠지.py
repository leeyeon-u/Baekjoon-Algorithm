import sys
N = int(input())

for i in range(N):
    student = 0
    X = list(map(int, sys.stdin.readline().split()))
    avg_value = sum(X[1:])/X[0]
    for j in X[1:]:
        if j > avg_value:
            student += 1
    avg_student = student/X[0]*100
    print(f"{avg_student:.3f}"+"%")
    student = 0
