H,M = map(int,input().split())

if M <45: #분 단위가 45분보다 작을 때
    if H==0: # 0시 이면
        H = 23
        M += 60
    else: # 0시가 아니면
        H -=1
        M +=60

print(H,M-45)