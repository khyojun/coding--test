import sys
def input(): return sys.stdin.readline().rstrip()
n, m = map(int, input().split())
pokemon={}
pokemon_num={}
problem=[]
for i in range(n):
    s=input()
    pokemon[s] = i+1
    pokemon_num[i+1] = s

for i in range(m):
    problem.append(input())

for i in range(len(problem)):
    if problem[i][0] >='A' and problem[i][0] <='Z':
        print(pokemon[problem[i]])
        continue
    print(pokemon_num[int(problem[i])])
