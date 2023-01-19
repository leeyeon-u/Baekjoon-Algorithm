import sys
cnt_sum = 0
while True:
    try:
        num = sys.stdin.readline()
        if int(num) < 10:
            num_copy = num
            num = str(0) + num
            while True:
                new_num = num[1] + str(int(num[0]) + int(num[1]))
                if (int(num[0]) + int(num[1])) > 9 :
                    new_num = num[1] + (str(int(num[0]) + int(num[1])))[1]
                cnt_sum += 1
                num = new_num
                if int(num) == int(num_copy):
                    print(cnt_sum)
                    cnt_sum = 0
                    break
        elif int(num) >= 10:
            num_copy = num
            while True:
                new_num = num[1] + str(int(num[0]) + int(num[1]))
                if (int(num[0]) + int(num[1])) > 9 :
                    new_num = num[1] + (str(int(num[0]) + int(num[1])))[1]
                cnt_sum += 1
                num = new_num

                if int(num) == int(num_copy):
                    print(cnt_sum)
                    cnt_sum = 0
                    break
    except:
        break