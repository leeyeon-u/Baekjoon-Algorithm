# isalpha() 연산자와 알파벳 구분 가능
# pop 사용

median_notation = list(input())
stack = []
result = ""

for i in median_notation:
    if i.isalpha():
        result += i
    else:
        if i == "(":
            stack.append(i)
        elif i == "*" or i == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                result += stack.pop()
            stack.append(i)
        elif i == "+" or i == "-":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()
while stack:
    result += stack.pop()

print(result)
