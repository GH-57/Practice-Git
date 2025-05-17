# # y, m, d = input().split('.')gh

# # print(d,m,y, sep="-")


# sep 는 ~으로 구분한다

# a, b = input().split("-")
# print(a, b, sep = "")


# s = input()
# print(s[0:2], s[2:4], s[4:])

# a,b,c = input().split(':')
# print(b)

# a, b = input().split("\t")
# c = float(a+b)
# print(c)

# a = float(input())
# b = float(input())
# print(a+b)

# a = int(input())
# b = int(input())
# a < b = True
# a >= b = False

# print(bool(a,b))

# n = input()

# if n == "A":
#     print("best!!!")
# elif n == "B":
#     print("good!!")
# elif n == "C":
#     print("run!")
# elif n == "D":
#     print("slowly~")
# else:
#     print("what?")

# a = int(input())
# b = int(input())
# print(a+b)

# R1, S = map(int, input().split())
# R2 = 2 * S - R1
# print(R2)

# N, M = map(int, input().split())
# print(N * M - 1)

# T = int(input())

# for i in range(1,T+1):
#     a,b = map(int,input().split())
#     print(f"Case #{i}: {a} + {b} = {a+b}")

# a = int(input())
# if a == 12 or a == 1 or a == 2:
#     print("winter")
# elif a == 3 or a == 4 or a == 5:
#     print("spring")
# elif a == 6 or a == 7 or a == 8:
#     print("summer")
# elif a == 9 or a == 10 or a == 11:
#     print("fall")



# n = int(input())
# sum = 0

# for i in range(1, n+1):
#     sum += i

# print(sum)


# X = int(input())
# N = int(input())
# sum = 0

# for i in range(N):
#     a, b = map(int,input().split())
#     sum += a * b
# if X == sum:
#     print('Yes')

# else:
#     print("No")



# n = int(input())

# for i in range(1, (n+1)):
#     print('*' * i)

# n = int(input())

# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*i )



# def f():
#     print('hello')

# f()


# def f():
#     print('**')

# f()



# while True:
#     a, b = map(int, input().split())
#     if (a == 0 and b == 0):
#         break
#     else:
        # print(a + b)


while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
