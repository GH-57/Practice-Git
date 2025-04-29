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



A,B = input().split()	 

print(int(A)+int(B))