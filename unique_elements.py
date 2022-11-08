n=int(input())
li=list(map(int,input().split()))
l=[]
for i in li:
    if i in l:
        pass
    else:
        l.append(i)
print(*l)        