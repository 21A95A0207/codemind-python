s=input()
sp=s.split()
count=0
l=[]
for i in sp:
    count=0
    for j in i:
        if i.isspace():
            pass
        else:
            count+=1
    l.append(count)        
print(*l)    