n=int(input())
ele=list(map(int,input().split()))
count=0
for i in range(0,n):
    if ele[i]%2 !=0:
        od_num=ele[i]
    else:
        count+=1
print(od_num)        