n=int(input())
m=list(map(int,input().split()))
c=[]
for i in range(0,len(m)):
    c.append(len(str(abs(m[i]))))
print(*c)    
    