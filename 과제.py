# 문제1(O)
'''
a = input()
print(f"안녕하세요, {a}님!")
'''

# 문제 2(O)
'''
a = input()
print(a*3)
'''

# 문제 3(O)
'''
a = int(input())
print(f"당신의 나이는 {2025-a}세입니다")
'''

# 문제 4(O)
'''
a = int(input())
b = a**2*3.14
print(f"반지름이 {a}인 원의 넓이: {b}")
'''

# 문제 5(O)
'''
a = int(input())
b = int(input())
c = a*b
print(f"총 이동 거리: {c}km")
'''

# 문제 6(O)
'''
a = input()
b = input()
print(f"{a} {b}")
'''

# 문제 7(O)
'''
a = int(input())
b = 2.54
print(f"{a}인치는 {a*b}센티미터입니다.")
'''

# 문제 8(O)
'''
a = int(input())
b = int(input())
c = int(a*(b/100))
print(f"팁 금액: {c}원 \n총 지불 금액: {a+c}원")
'''

# 문제 9(O)
'''
a = int(input())*0.01
b = int(input())
c = b/(a**2)
print(f"BMI: {c:.2f}")
'''

# 문제 10 (질문)(*)
'''
a = map(int,input().split())
b = list(a)
## a = list(map(int, input().split()))
print(f"첫 번째 숫자: {b[0]} \n마지막 숫자: {b[-1]}")
'''

# 문제 11(O)
'''
a = int(input())
b = int(input())
a,b = b,a
print(f"교환 전: a = {a}, b = {b}\n교환 후: a = {b}, b = {a}")
'''

# 문제 12(O)
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
# 문제 14(o)
'''
a = float(input())
print(f"{a:.2f}")
'''

# 문제 15(O)
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
# 문제 18(O)
'''
a = int(input())

if a%2 == 0: #짝수이면
    print(f"{a}은(는) 짝수입니다.")
else:
    print(f"{a}은(는) 홀수입니다.")
'''    
# 문제 19(O)
'''
a,b,c,d = input().split()
A = [a,b,c,d]
print(','.join(A))
'''

# 문제 20(O)
# °C °F
# a가 섭씨라면, 화씨는 (a-32)*5/9이다
# a가 화씨라면, 섭씨는 a*9/5+32이다
'''
a = int(input())
b = input() 

if b == "C":
    print(f"{float(a)}°C는 {(a*9/5)+32}°F입니다.")
elif b == "F":
    print(f"{a}°F는 {((a-32)*5/9)}°C입니다.")
'''

# 문제 21(O)
'''
a = input()
b = a.upper()
c = a.lower()
d = a.title()

print(f"대문자: {b}")
print(f"소문자: {c}")
print(f"첫 글자만 대문자: {d}")
'''

# 문제 22(O)
'''
a = input()
print(f"앞 3글자: {a[0:3]}")
print(f"뒤 3글자: {a[-3:]}")
print(f"거꾸로: {a[::-1]}")
'''

# 문제 23 (?) # 출력 예시가 잘못된건가...?
'''
a = input()
b = input()
# c = a.count(' ') # 공백의 수

print(f"단어 '{b}'의 위치: {a.find(b)}")
'''

# 문제 24(O)
'''
a = input()
b = input()
c = input()
print(a.replace(b,c))
'''

# 문제 25(O)
'''
a = input()
b = input()
print(f"문자 '{b}'의 출현 횟수: {a.count(b)}")
'''

# 문제 26(O)
'''
a = input()
if "@" in a:
    print("유효한 이메일 주소입니다.")
else:
    print("유효하지 않은 이메일 주소입니다.")
'''

# 문제 27 
# ##ljulst() 사용인가..? (지정한 길이만큼 왼쪽정렬)
'''
a = input()
b = int(input())
c = b-len(a) # 문자열의 현재길이 - 원하는 길이
print(a.ljust(b, '*'))
'''

# 문제 28(O)
'''
a = input()
b = len(a)
if b%2 == 0: # 짝수이면
    print(f"중앙 문자: {a[b//2-1]}{a[b//2]}")
else:
    print(f"중앙 문자: {a[b//2]}")
'''

# 문제 29(O)
'''
a = input()
b = a.replace(',','')
c = b.replace('!','')
d = c.replace('?','')
print(d)
'''

# 문제 30(O)
'''
print("그녀가 말했다: \"안녕하세요!\"\n이름 나이 직업\n홍길동 30\t개발자\n안녕!\n반가워요!")
'''

# 문제 31