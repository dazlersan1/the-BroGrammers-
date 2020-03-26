from math import *
n,k=map(int,input().split())

a=list(map(int,input().split()))

mod=[0 for i in range(k)]

for i in a:
    mod[i%k]+=1

count=0

if(mod[0]==0):
    pass
else:
    count=1
for i in range(1,ceil(k/2)):
    
        count=count+max(mod[i],mod[k-i])
        

if(k%2==0):
    
    
    if(mod[k//2]>0):
        
        count=count+1
print(count)
