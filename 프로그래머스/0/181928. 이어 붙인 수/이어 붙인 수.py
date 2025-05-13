def solution(num_list):
    짝수 = ''
    홀수 = '' 
    for i in num_list:
        if i % 2 == 0:
            짝수 += str(i)
        else:
            홀수 += str(i)
    answer = int(짝수) + int(홀수)
    return answer

solution([3, 4, 5, 2, 1])