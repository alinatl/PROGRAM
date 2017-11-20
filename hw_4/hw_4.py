with open("text.txt", encoding="utf-8") as f: 
    text = f.read() 
    splited_text = text.split() 
j=0 
for i in splited_text: 
    if i[0].isupper(): 
        j+=1 
answer=(j*100)//len(splited_text) 
print(answer,"%")
