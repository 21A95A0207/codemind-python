n=int(input())
li=list(map(int,input().split()))
c=0
avg=sum(li)/n
for i in li:
    if i<=avg:
        c+=1
print(c)        