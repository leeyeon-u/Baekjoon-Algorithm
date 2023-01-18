total_price = int(input())
kinds = int(input())
total_list = []

while True:
    price, num = list(map(int,input().split()))
    value = price*num
    total_list.append(value)
    kinds -= 1
    if kinds == 0:
        break
if sum(total_list) == total_price:
    print("Yes")
else:
    print("No")
