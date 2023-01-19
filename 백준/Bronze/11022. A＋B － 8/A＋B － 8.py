import sys
total_sum =  int(sys.stdin.readline())

while True:
    for i in range(1,total_sum+1):
        first_num, second_num =  list(map(int,sys.stdin.readline().split()))
        sum_result = first_num + second_num
        print("Case #" + str(i) +":", first_num, "+", second_num, "=", sum_result)
        total_sum -= 1
    if total_sum == 0:
        break
