n=int(input())
l=list(map(int,input().split()))
rev=0
newlist=[]
for i in l:
    while i>0:
        rev=rev*10+i%10
        i=i//10
    newlist.append(rev)
    rev=0
print(*newlist)    