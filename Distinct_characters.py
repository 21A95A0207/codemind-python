s=input()
s1=''.join(s.split())
s2=s1.lower()
s3=set(s2)
l=[]
for i in s3:
    if i in s2:
        l.append(i)
l.sort()
for k in l:
    print(k,end='')
