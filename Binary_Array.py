n=int(input())
l=list(map(int,input().split()))
for i in range(2,10):
    if i in l:
        print('False')
        break
    else:
        print('True')
        break
