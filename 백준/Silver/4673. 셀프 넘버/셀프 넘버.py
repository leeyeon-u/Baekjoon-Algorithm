# 자연수
natural_num = set(range(1, 10001))
# 생성자
generated_num = set()

for i in natural_num:
    for j in str(i):
        i += int(j)
    if i <= 10000:
        generated_num.add(i)

self_num = sorted(natural_num-generated_num)

for k in self_num:
    print(k)