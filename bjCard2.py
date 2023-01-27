import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque


# 일반적인 파이썬에서는 pop연산자는 O(n)의 시간만큼 걸리게 됨

queue=deque()

n= int(input())

for i in range(n):
    queue.append(i+1)

while(len(queue)>1):
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])

