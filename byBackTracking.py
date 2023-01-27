
import sys
def input(): return sys.stdin.readline().rstrip()

n, m = map(int, input().split())



def trace(now, n, length, arr):
    if len(arr)==length:
        for i in range(len(arr)):
            print(arr[i], end=' ')
        print()
        return
    
    for now in range(now, n+1):
        arr.append(now)
        trace(now, n, length, arr)
        arr.pop()



arr=[]
trace(1, n, m, arr)