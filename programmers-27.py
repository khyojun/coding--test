def solution(price, money, count):
    answer = -1
    s=0
    for i in range(1, count+1):
        s+=price*i
    
    if money<s:
        return s-money
    else:
        return 0
        