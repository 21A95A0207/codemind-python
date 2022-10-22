s=input()
s1=''.join(s.split())
s2=s1.lower()
s3=set(s2)
k=0
for i in s3:
    count=0
    for j in s2:
        if j==i:
            count+=1
    if count>1:
        pass
    else:
        k+=1
print(k)        
        
    
