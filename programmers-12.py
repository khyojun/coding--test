from itertools import permutations
import math


def isPrime(n):
    if n<2:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


def solution(numbers):
    answer = 0
    is_prime=[]
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            tmp="".join(j)
            num_tmp=int(tmp)
            
            if isPrime(num_tmp) and (not num_tmp in is_prime):
                is_prime.append(num_tmp)
                answer+=1
    return answer