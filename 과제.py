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

########### 문제 13(하드)
'''
name = input().split()
a = str(n")
'''
############
# 문제 14
'''
a = float(input())
print(f"{a:.2f}")
'''

# 문제 15
'''
a = int(input())

if a >= 65:
    print("노년")
elif a >= 35:
    print("중장년")
elif a >= 19:
    print("청년")
else:
    print("미성년자")
'''

####################### 문제 16(하드)
'''
a = input().split()
b = list(a)

# if ' ' in b and int(b) in b:
print(f"공백 수: {len(' ')}\n숫자 수: {b.count(int)}\n문자 수: {len(b)}")
'''
############################
# 문제 17(질문)
'''
a = int(input())
b = int(input())
c = input()
d = input()
e = input()
f = input()

if a == 0:
    print(bool(a))
elif a !=0:
    print(bool(a))
if b == 0:
    print(bool(b))
elif b !=0:
    print(bool(b))
if c == '""':
    print(bool(c))
elif c!= '""':
    print(bool(c)) ## 어디서 안되는 건지..
if d == "":
    print(bool(d))
elif d!= "":
    print(bool(d))
if e == "":
    print(bool(e))
elif e!= "":
    print(bool(e))
if f == "":
    print(bool(f))
elif f!= "":
    print(bool(f))
'''
# 문제 18
'''
a = int(input())

if a%2 == 0: #짝수이면
    print(f"{a}은(는) 짝수입니다.")
else:
    print(f"{a}은(는) 홀수입니다.")
'''    
# 문제 19
s = input().split
a = list(s)

','.join(a)
