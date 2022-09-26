s=input()
k=s.split()
v='AEIOUaeiou'
count=0
for i in k:
    if i[0] in v and i[-1] not in v:
        count+=1
print(count)        