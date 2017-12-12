count = 0
with open ('C:/Users/User/AppData/Local/Programs/Python/Python36-32/Extinct_languages.tsv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split("	")
        if "Critically endangered" in words[2]:
            count += 1
    print('число Critically endangered=',count)
