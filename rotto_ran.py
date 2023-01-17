import random


n=int(input("복권 몇 장?"))
for page in range(n):
    print(page+1 , "번째 장입니다.")
    for i in range(5):
        rottery_lis=[]
        rottery_lis=set()
        while rottery_lis.__len__()<6:
            rottery_lis.add(random.randint(1,45))
        print(rottery_lis)