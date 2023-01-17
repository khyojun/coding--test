import sys
def input(): return sys.stdin.readline().rstrip()

n=int(input())

a=[]
sequence=[]
stack=[]
for i in range(1,n+1):
    a.append(i)

for i in range(n):
    sequence.append(int(input()))

print_stack=[]
success=False
while(True):
    if len(sequence)==0 and len(stack)==0:
        success=True
        break
    if len(stack)>0 and stack[len(stack)-1] == sequence[0]:
        print_stack.append("-")
        stack.pop(len(stack)-1)
        sequence.pop(0)
        continue
    if len(a)>0:
        now=a.pop(0)
        stack.append(now)
        print_stack.append("+")
        continue
    break

if success:
    for i in range(len(print_stack)):
        print(print_stack[i])

else:
    print("NO")
    


    
