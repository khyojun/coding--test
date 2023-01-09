def solve(n, m, div):
    if m==1:
        return n
    else:
        result=solve(n,m//2, div)
        if m%2!=0:
            return (result*result*n)%div
        else:
            return (result*result)%div 



a, b, c=map(int, input().split())

cnt=0
result=0
result= solve(a,b,c)%c



print(result)