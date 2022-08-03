def swap(a,b): #최소직사각형
    tmp=0
    tmp=a
    a=b
    b=tmp
    
    return a,b


def solution(sizes):
    answer = 0
    w=[]
    h=[]
    for i in range(len(sizes)):
        w.append(sizes[i][0])
        h.append(sizes[i][1])
        if w[i]<=h[i]:
            w[i], h[i]=swap(w[i], h[i])
    
    return max(w)*max(h)