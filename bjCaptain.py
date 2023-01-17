dp=[]

dp=[0,1,2,3]
n=int(input())
now_count=3
cnt=0
for i in range(4, n+1):
   dp.append(((dp[i-1]% 15746)+(dp[i-2]% 15746))% 15746)




print(dp)
print(dp[n])
