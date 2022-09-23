n=int(input())
l=list(map(int,input().split()))
li=[]
for i in range(0,n):
    li.append(len(str(abs(l[i]))))

print(li.count(max(li)))    