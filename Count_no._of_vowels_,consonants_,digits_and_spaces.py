s=input()
Vowels=0
Consonants=0
Digits=0
White_spaces=0
v=('AEIOUaeiou')
for i in range(0,len(s)):
    if s[i] in v:
        Vowels+=1
    elif s[i]==' ':
        White_spaces+=1
    elif s[i].isdigit():
        Digits+=1
    else:
        Consonants+=1

print('Vowels:',Vowels)
print('Consonants:',Consonants)
print('Digits:',Digits)
print('White spaces:',White_spaces)
        