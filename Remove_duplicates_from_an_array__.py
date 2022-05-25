n=int(input())
li=list(map(int,input().split()))
nli=[]
for i in li:
    if i not in nli:
        nli.append(i)
print(*nli)        