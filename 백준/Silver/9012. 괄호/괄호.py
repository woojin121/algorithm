import sys

def is_valid_parenthesis(s):
    stack = []  # 스택을 사용하여 괄호를 처리할 예정

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # 스택이 비어있는데 닫는 괄호가 나온 경우
                return "NO"
            stack.pop()

    if not stack:  # 모든 열린 괄호에 대응되는 닫힌 괄호가 있어야 함
        return "YES"
    else:
        return "NO"

# 테스트 케이스의 개수 입력
T = int(input())

for _ in range(T):
    input_string = input()
    result = is_valid_parenthesis(input_string)
    print(result)