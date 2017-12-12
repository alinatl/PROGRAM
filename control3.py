# не успела дописать 
opr = []
with open ('C:/Users/User/AppData/Local/Programs/Python/Python36-32/Extinct_languages.tsv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    word = None
    while word != '':
        word = input ("""
        ведите название языка.
        нажмите энтер для окончания""")
        for line in lines:
            words = line.split("	")
            line.replace("\t", "")
            if word in words[0]:
                opr.append(line)
            print (opr)
            word = input ("""
        ведите название языка.
        нажмите энтер для окончания""")
            line = None
            
            
            
