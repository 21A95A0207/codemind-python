n=int(input())
li=list(map(int,input().split()))
count=0
for i in li:
    temp=i
    rev=0
    while i>0:
        rev=rev*10+i%10
        i=i//10
    if rev==temp:
        count+=1
print(count)        
    