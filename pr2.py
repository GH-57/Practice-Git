# # code up 연습문제
# ## 6044
# a,b = input().split()
# a,b = int(a),int(b)
# c = a+b # 합
# d = a-b # 차
# e = a*b # 곱
# f = a//b # 몫
# g = a%b # 나머지
# h = a/b # 나눈값
# print(f"{c}\n{d}\n{e}\n{f}\n{g}\n{h:.2f}")

# 6049
# a,b = input().split()
# a,b = int(a),int(b)
# if a < b:
#     print(True)

# elif a >= b:
#     print(False)

# a,b = input().split()
# a,b = int(a),int(b)
# if a == b:
#     print(True)

# elif a != b:
#     print(False)

# a = int(input())
# print(bool(not a))

# a,b = input().split()
# c,d = bool(int(a)), bool(int(b))

# print((c and (not d)) or ((not c) and d)) 
# --서로 다를 때에만 True출력--

# a,b = input().split()
# c,d = bool(int(a)), bool(int(b))

# print(not(c or d))


# a = int(input())

# if a<0:
#     if a%2==0 :
#         print("A")

#     else:
#         print('B')
# else:    
#     if a%2==0 :
#         print("C")

#     else:
#         print("D") 
# # 



# n=int(input())

# if n<0:
#   if n>=:
#     print('A')
#   else:
#     print('B')
# else:
#   if n%2==0:
#     print('C')
#   else:
#     print('D')



# A,B = input().split()

# print(int(A)+int(B)
      
# A,B = input().split()	 

# print(int(A)-int(B)

# a = input()
# print(a + "??!")

# 불기-서기=543

# a = int(input())
# print(a-543)

# A,B,C = input().split()
# A = int(A)
# B = int(B)
# C = int(C)

# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))%C)

# a = int(input()) #1
# b = input() #2

# print(a*int(b[2]))  #3
# print(a*int(b[1]))  #4
# print(a*int(b[0]))  #5
# print(a*int(b)) #6

# print("\\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")

# print("|\\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print("||_/=\\\\__|")

# x = int(input())
# y = int(input())

# if x >0 and y >0:
#     print('1')
# elif x <0 and y >0:
#     print('2')
# elif x <0 and y <0:
#     print('3')
# else:
#     print('4')

# H,M = map(int,input().split())

# if M <45: #분 단위가 45분보다 작을 때
#     if H==0: # 0시 이면
#         H = 23
#         M += 60
#     else: # 0시가 아니면
#         H -=1
#         M +=60

# print(H,M-45)

# h, m = map(int, input().split()) # 시, 분 입력
# t = int(input()) # 필요한 분 입력

# h += t // 60  # 시는 60으로 나눈 몫
# m += t % 60 # 분은 60으로 나눈 나머지

# if m >= 60:  # 분이 60 넘어간다면
#     h += 1   # 시는 1씩 추가
#     m -= 60  # 분은 60씩 빼기
# if h >= 24:  # 시가 24 넘어간다면
#     h -= 24  # 시는 24씩 빼기

# print(h, m)


# a = input()
# b = int(input())
# print(a[b-1])

# a = input()
# print(len(a))

# a = input()
# b = input()
# c = input()

# print(a)
# print(b)
# print(c)



# a = int(input())

# for i in range(1, 10):
#     print(a, "*", i, "=", a*i)

# a = int(input())

# for i in range(a):
#     test = input()
#     print(test[0]+test[-1])

# a = int(input())

# for i in range(a):
#     a,b = map(int,input().split())
#     print(a+b)



# num = input() # 숫자의 개수
# numbers = list(map(int,input())) # 리스트로 숫자들을 입력받는다

# print(sum(numbers)) # list number의 합을 구한 후, 출력