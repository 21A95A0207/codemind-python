st=input()
count=0
for i in range(len(st)):
    if (ord(st[i])) >=97 and (ord(st[i])) <= 122:
        count+=1
print(count)        
