N = int(input())
A_list = []
B_list = []
for i in range(N):
    N_list = list(input())
    sum_value = 0
    for j in range(len(N_list)):
        if N_list[j] == 'O':
            sum_value += 1
        else:
            sum_value = 0
        A_list.append(sum_value)
    print(sum(A_list))
    A_list = []