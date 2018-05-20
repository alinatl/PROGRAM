import os

def f_type(string):
    #возвращает тип файла
    k=1
    for j in reversed(string):
        if j != '.':
            k+=1
        else:
            string = string[len(string)-k+1:]
            return string

direct =[]
start_path = '.'
for root, dirs, files in os.walk(start_path):
    freq = {}
    direct.append(freq)
    for file in files:
        if f_type(file) in freq:
            freq[f_type(file)] += 1
        else:
            freq[f_type(file)] = 1
frq = {}
for dictionary in direct:
    for i in dictionary:
        if dictionary[i]>=2:
            if i in frq:
                    frq[i] += 1
            else:
                frq[i] = 1
#Вывод количества папок, содержащих несколько одинаковых типов файлов
for i in frq:
    print("There are", frq[i], "directories with some", i, "files")
