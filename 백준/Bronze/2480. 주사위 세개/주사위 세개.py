A, B, C = list(map(int,input().split()))
listA = [A, B, C]

if A == B == C:
    print(10000 + (A*1000))
elif A == B or A == C:
    print(1000 + (A * 100))
elif B == C:
    print(1000 + (B * 100))
else:
    print(max(listA)*100)