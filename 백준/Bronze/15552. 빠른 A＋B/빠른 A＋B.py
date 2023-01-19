import sys
total_sum =  int(sys.stdin.readline())

while True:
    first_num, second_num =  list(map(int,sys.stdin.readline().split()))
    sum_result = first_num + second_num
    print(sum_result)
    total_sum -= 1
    if total_sum == 0:
        break
