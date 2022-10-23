s1=input()
s2=input()
s3=s1.lower()
s4=s2.lower()
s5=''.join(s3.split())
s6=''.join(s4.split())
l=[]
for i in s5:
    for j in s6:
        if j==i:
            if i in l:
                pass
            else:
                l.append(i)
print(len(l))                