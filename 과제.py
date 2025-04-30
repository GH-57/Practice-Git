# 문제1
'''
a = input()
print(f"안녕하세요, {a}님!")
'''

# 문제 2
'''
a = input()
print(a*3)
'''

# 문제 3
'''
a = int(input())
print(f"당신의 나이는 {2025-a}세입니다")
'''

# 문제 4
'''
a = int(input())
b = a**2*3.14
print(f"반지름이 {a}인 원의 넓이: {b}")
'''

# 문제 5
'''
a = int(input())
b = int(input())
c = a*b
print(f"총 이동 거리: {c}km")
'''

# 문제 6
'''
a = input()
b = input()
print(f"{a} {b}")
'''

# 문제 7
'''
a = int(input())
b = 2.54
print(f"{a}인치는 {a*b}센티미터입니다.")
'''

# 문제 8
'''
a = int(input())
b = int(input())
c = int(a*(b/100))
print(f"팁 금액: {c}원 \n총 지불 금액: {a+c}원")
'''

# 문제 9
'''
a = int(input())*0.01
b = int(input())
c = b/(a**2)
print(f"BMI: {c:.2f}")
'''

# 문제 10 (질문)
'''
a = map(int,input().split())
b = list(a)
## a = list(map(int, input().split()))
print(f"첫 번째 숫자: {b[0]} \n마지막 숫자: {b[-1]}")
'''

# 문제 11
'''
a = int(input())
b = int(input())
a,b = b,a
print(f"교환 전: a = {a}, b = {b}\n교환 후: a = {b}, b = {a}")
'''

# 문제 12
'''
a = list(input())
b = len(a)
print(f"문자열 길이: {b}\n첫 글자: {a[0]}\n마지막 글자: {a[-1]}")
'''

# 문제 13(하드)
a = input().split()
b = a