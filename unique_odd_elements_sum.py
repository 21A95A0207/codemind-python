n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    if i%2!=0 and i not in li:
        li.append(i)
print(sum(li))        