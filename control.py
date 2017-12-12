with open ('C:/Users/User/AppData/Local/Programs/Python/Python36-32/Extinct_languages.tsv', 'r', encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')
for word in lines:
    count = len(word)
    if count > 35:
        print(word)
    else:
        continue



