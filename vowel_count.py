s=input()
v="AEIOUaeiou"
count=0
for i in s:
    if i in v:
        count+=1
    else:
        pass
if count==0:
    print('0')
else:
    print(count)