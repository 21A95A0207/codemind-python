n=int(input())
m=list(map(int,input().split()))
li=[]
for i in range(0,n):
    li.append(len(str(abs((m[i])))))
    
print(li.count(min(li)))