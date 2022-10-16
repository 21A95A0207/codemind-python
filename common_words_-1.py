s1=input()
s2=input()
s=s1.lower()
s0=s2.lower()
k=s.split()
l=s0.split()
count=0
for i in k:
    for j in l:
        if i==j:
            count+=1
print(count)            