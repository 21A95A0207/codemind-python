n=int(input())
li=list(map(int,input().split()))
l=[]
for i in li:
    if i%2==0 and i not in l:
        l.append(i)
print(len(l))        