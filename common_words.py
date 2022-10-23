s=input()
s1=input()
s2=s.lower().split()
s3=s1.lower().split()
l=[]
for i in s3:
    for j in s2:
        if j==i:
            l.append(i)
print(*l)            