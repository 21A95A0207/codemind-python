st=input()
count=0
for i in range(len(st)):
    if ord(st[i]) >=65 and ord(st[i]) <= 90:
        count+=1
print(count)        