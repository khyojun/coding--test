import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

n=int(input())
stack=deque()
for i in range(n):
    gwalo=input()
    for j in range(len(gwalo)):
        stack.append(gwalo[j])
        if gwalo[j]==")":
            if len(stack)-2>=0 and stack[len(stack)-2]=="(":
                stack.pop()
                stack.pop()
    if len(stack)>0:
        print("NO")
    else:
        print("YES")
    stack.clear()   

    