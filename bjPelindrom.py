import sys
def input(): return sys.stdin.readline().rstrip()
while(True):
    n=input()
    if n=="0":
        break
    front = n
    back = n[::-1]

    if front == back:
        print("yes")
    else:
        print("no")

