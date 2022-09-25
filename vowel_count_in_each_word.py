s=input()
sp=s.split()
v='AEIOUaeiou'
l=[]
for i in sp:
    count=0
    for j in i:
        if j in v:
            count+=1
    l.append(count)        
print(*l)            