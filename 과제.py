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
# 쓰는 방법...?
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
a = int(input())  ## 정수형이 아니다!
b = input() 

if b == "C":
    print(f"{float(a)}°C는 {(a*9/5)+32}°F입니다.")
elif b == "F":
    print(f"{a}°F는 {((a-32)*5/9)}°C입니다.")
'''
## 강사님 해설 (20번)
'''
temp = input()
temp = float(temp)
unit = input() # C 또는 F

if unit == "C": # 섭씨라면
    convert = temp * 9/5 + 32
    print(f"{temp}.C는 {convert}.F입니다.")
elif unit == "F": #화씨라면
    convert = (temp-32) * 5/9
    print(f"{temp}.F는 {convert}.C입니다.") 
else:
    print("잘못입력하였습니다")
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

# 문제 23 (?) # 출력 예시가 잘못된건가...? [if문 사용해라]
'''
a = input()
b = input()
# c = a.count(' ') # 공백의 수

print(f"단어 '{b}'의 위치: {a.find(b)}")
'''
##강사님 해설(23번) [if문 사용해라]
'''
sentence = input() # 문장입력
word = input() # 단어입력

position = sentence.find(word) # 문장 안에서 단어를 찾는다

if position != -1: # 찾았다.
    print(f"단어 '{word}'의 위치: {position}")
else:
    print(f"단어 '{word}'를 찾을 수 없습니다.")
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

# 문제 31(O)
'''
a = int(input())
b = int(input())
c = input()

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
else:
    print(a/b)
'''

# 문제 32(O)
'''
a = int(input())
b = int(input())
c = a*(b/100)
print(f"세금:{c}원")
print(f"세후 금액: {a-c}원")
'''

# 문제 33(o)
'''
a = True
b = False
print(f"{a} AND {b} = {a and b}")
print(f"{a} OR {b} = {a or b}")
print(f"NOT {a} = {not a}")
print(f"NOT {b} = {not b}")
'''

# 문제 34(O
'''
a = int(input())
b = int(input())
c = a*(b/100)
print(f"할인 금액: {c}원")
print(f"최종 가격: {a-c}원")
'''

# 문제 35(O)
'''
a = int(input())
b = int(input())
c = int(input())
d = [a,b,c]
e = max(d)
print(f"가장 큰 수: {e}")
'''

# 문제 36(O)
'''
a = int(input())

if (a%4 == 0 and a%100 !=0) or a%400 == 0:
    print(f"{a}년은 윤년입니다")
else:
    print(f"{a}년은 윤년이 아닙니다")
'''

# 문제 37(O)
'''
a = input()
b = input()

if b in a:
    print(f"\"{a}\"에 \"{b}\"이(가) 포함되어 있습니다. ")
else:
    print(f"\"{a}\"에 \"{b}\"이(가) 포함되어 있지 않습니다. ")
'''

# 문제 38(O)
'''
a = int(input())

if a >= 90:
    print(f"학점: A")
elif a >= 80:
    print(f"학점: B")
elif a >= 70:
    print(f"학점: C")
elif a >= 60:
    print(f"학점: D")
else:
    print(f"학점: F")
'''

# 문제 39(구글링 통해 맞추긴 했는데 모르겠음)
## for함수 쓰는 방법
'''
a = input()
b = sum(int(a) for a in a)
print(f"자릿수 합계: {b} ")
'''
## 10으로 계속 나누어 나머지를 더하는 방식(구글링)
'''
number = int(input())

sum = 0
sum = sum + number % 10
number = number // 10
sum = sum + number % 10
number = number // 10
sum = sum + number % 10
number = number // 10
sum = sum + number % 10
number = number // 10
print("자릿수의 합:", str(sum))
'''

# 문제 40(O)
'''
a = int(input())
b = input()

if a >= 19 and b == "N":
    print("입장료: 10000원")
elif a >= 19 and b == "Y":
    print("입장료: 8000원")
else:
    print("입장료: 5000원")
'''

# 문제 41(O)
'''
a = input()
A = a.isalnum() ## 문자열이 (영어 한글 숫자)이면 "참" 아니면 "거짓"
if len(a) >= 8 and A:
    print("안전한 비밀번호입니다.")
else:
    print("안전하지 않은 비밀번호입니다.")
'''

# 문제 42(??????)
'''
### (잘못된 풀이)
words = input() # 입력받은 문장

for _ in range(1): # 한 문장동안 반복?
    revers = [] #뒤집은 문자 모아둘 리스트 

for word in words: # 입력받은 문장을 단어로 분리
    revers.append(words[::-1]) # 뒤집은 단어들 추가

a = " ".join(revers)
print(a)

### (구글링한 풀이)
n = 1

for i in range(n):
    s = list(input().split())
    for j in s:
        print(j[::-1], end=" ")
    print()
'''

# 문제 43(????)
'''
word = list(map(str, input()))

vowels = ["a", "e", "i", "o", "u"]
count = 0

for letter in word:
    if letter in vowels:
        count += 1
        
print(f"모음 개수: {count}")
print(f"자음 개수: {len(word)-count-1}")
'''

# 문제 44 (O)
## round 함수는 round(값, 소수점 자리)
'''
a = float(input())

print(f"가장 가까운 정수: {round(a)}")
'''

# 문제 45(????)
'''
a = input().split("-")

yyyy = a[0] #년
mm = a[1] #월
dd = a[2] #일
if yyyy % 4 == 0 and yyyy%100 !=0 or yyyy%400 == 0: #윤년 일 때 
    if (mm == 4,6,9,11 and 1<=dd<=30) and (mm == 2 and 1<=dd<=29): 
        print(f"유효한 날짜입니다.")
elif yyyy % 4 == 0 and yyyy%100 !=0 or yyyy%400 == 0: #윤년 일 때
    if (mm == 1,3,5,7,8,10,12 and 1<=dd<=31):
        print(f"유효한 날짜입니다.")
else: 
    print("유효하지 않은 날짜 입니다.")
'''    

# 문제 46(O)
'''
a = input().split(".")

print(f"확장자: {a[1]}")
'''

# 문제 47 (?????)
## (정답은 알아도 설명할 수 있나?)
'''
def compress_string(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count)) # 마지막 문자 붙이기
    return ''.join(compressed)

print(compress_string(input()))  
'''

# 문제 48(O)
'''
a = input()

if a == a[::-1]:
    print(f"'{a}'은(는) 팰린드롬입니다.")
else:
    print(f"'{a}'은(는) 팰린드롬이 아닙니다.")
'''

# 문제 49(????)
#####(와 이건 진짜 모르겠다)
'''
a = list(input())
b = []
a[0] = H
'''


# 문제50
################### 일부 구글링한 것
'''
a = input().split(".") # ip를 입력받아 .으로 분리
b = list(map(int,a)) #ip를 int로 형변환(구글링)
## a[0] a[1] a[2] a[3]
c = b[0] 
d = b[1] 
e = b[2] 
f = b[3]


if (0<=c<=255 and 0<=d<=255 and 0<=e<=255 and 0<=f<=255) and len(a) == 4:
    print(f"유효한 IP 주소입니다.")
else:
    print(f"유효하지 않은 IP주소입니다.")
'''

################### 내 풀이
'''
a = input().split(".") # ip를 입력받아 .으로 분리
## a[0] a[1] a[2] a[3]
c = a[0] 
d = a[1] 
e = a[2] 
f = a[3]

g = int(c)
h = int(d)
i = int(e)
j = int(f)

if (0<=g<=255 and 0<=h<=255 and 0<=i<=255 and 0<=j<=255) and len(a) == 4:
    print(f"유효한 IP 주소입니다.")
else:
    print(f"유효하지 않은 IP주소입니다.")
'''
