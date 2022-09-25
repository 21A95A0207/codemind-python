s=input()
spt=s.split()
l=[]
count=0
for i in spt:
    count=0
    for j in i:
        if i.isspace():
            pass
        else:
            count+=1
    l.append(count)
print(max(l))    
            