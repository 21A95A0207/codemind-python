n=int(input())
li=list(map(int,input().split()))
evl=[]
od=[]
for i in li:
    if i%2!=0:
        od.append(i)
    else:
        evl.append(i)
if evl==li:
    print('True')
else:
    print('False')