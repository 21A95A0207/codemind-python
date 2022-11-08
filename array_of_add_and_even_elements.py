n=int(input())
l=list(map(int,input().split()))
od=[]
ev=[]
for i in l:
    if i%2==0:
        ev.append(i)
    else:
        od.append(i)
opt=od+ev
print(*opt)        