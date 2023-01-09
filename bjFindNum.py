
def binarySearch(lo, hi, A,find):
    mid=(lo+hi)//2
    if mid>=len(A):
        return 0
    if lo>hi:
        return 0
    elif hi<lo:
        return 0

    if A[mid]==find:
        return 1
    elif A[mid]<find:
        return binarySearch(mid+1, hi, A, find)
    elif A[mid]>find:
        return binarySearch(lo, mid-1, A, find)
    






n=int(input())

A=list(map(int, input().split()))
m=int(input())
B=list(map(int, input().split()))
A.sort()
for i in range(len(B)):
    print(binarySearch(0, n-1, A, B[i]))





