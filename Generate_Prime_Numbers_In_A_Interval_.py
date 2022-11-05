std1=int(input())
std2=int(input())
for i in range(std1,std2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)