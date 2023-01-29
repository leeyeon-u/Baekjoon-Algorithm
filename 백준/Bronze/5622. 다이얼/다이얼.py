alpabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = list(input())

time = 0

for i in word:
    for j in alpabet:
        if i in j:
            time += alpabet.index(j) + 3

print(time)
