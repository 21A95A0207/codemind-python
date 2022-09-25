n,m=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(0,n):
    if len(str(abs(l[i])))==m:
        count+=1
print(count)        