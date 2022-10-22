s=input()
s1=''.join(s.split())
s2=s1.lower()
s3=set(s2)
l=[]
for i in s3:
    count=0
    for j in s2:
        if i==j:
            count+=1
    if count>1:
        pass
    else:
        l.append(i)
l.sort()
print(''.join(l))