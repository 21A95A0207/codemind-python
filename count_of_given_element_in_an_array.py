n=int(input())
elements=list(map(int,input().split()))
m=int(input())
count=0
for i in range(0,n):
    if m==elements[i]:
        count+=1
    else:
        count+=0
print(count)        