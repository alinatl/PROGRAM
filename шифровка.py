s=str(input())
alf='abcdefgefghijklmnopqrstuvwxyz'
for i in range (len(s)):
    for x in range(len(alf)):
        if s[i]==alf[x]:
            print(alf[x+1])
            break 
        elif s[i]==' ':
            continue
             

    
