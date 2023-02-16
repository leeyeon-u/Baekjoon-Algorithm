number = int(input())

honeycomb_num = 1
cnt = 1
while number > honeycomb_num :
    honeycomb_num += 6 * cnt
    cnt += 1
print(cnt)