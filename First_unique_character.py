s=input()
s1=''.join(s.split())
l=[]
for i in range(0,len(s1)):
    count=0
    for j in s1:
        if s1[i]==j:
            count+=1
    if count>1:
        pass
    else:
        l.append(s1[i])
        
if len(l)==0:
    print('-1')
else:
    print(l[0])
        