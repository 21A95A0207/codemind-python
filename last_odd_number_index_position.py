n=int(input())
ele=list(map(int,input().split()))
for i in range(0,n):
    if ele[i]%2 !=0:
        od_num=i
    
print(od_num)        