s=input()
split=s.split()
count=0
l=[]
for i in split:
    for j in i:
        if i.isspace():
            pass
        else:
            count+=1
    l.append(count)        
            
print(min(l))            