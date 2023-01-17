testcase_num=int(input())

for i in range(testcase_num):
    n, m = map(int,input().split())
    a = list(map(int, input().split()))
    list_max=max(a)
    index=m
    cnt=1
    while(len(a)>0):
        list_max=max(a)
        if list_max==a[0] and index==0:
            print(cnt)
            break
        elif list_max>a[0] and index==0:
            tmp=a.pop(0)
            a.append(tmp)
            index=len(a)-1
        elif list_max==a[0] and index!=0:
            a.pop(0)        
            index-=1
            cnt+=1
        elif list_max>a[0] and index!=0:
            tmp=a.pop(0)
            a.append(tmp)
            index-=1
            
