A, B = input().split()
C = int(input())
A = int(A)
B = int(B)

D = B + C


if D == 60:
    A = A + 1
    B = 0
elif D > 59:
    A = int((D/60) + A)
    B = D % 60
else:
    B = D

if A == 24:
    A = 0
elif A > 24:
    A = A-24
print(A, B)