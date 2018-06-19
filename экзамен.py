print('Задание 1\n')

import csv
import re
import os

def read_f():
    with open('C:/Users/User/Desktop/ПРОГРАММИРОВАНИЕ/PROGRAM/Новая папка/news/_itartass1.xhtml') as f:
        f = f.read()
        print(f)
    return f

def task(f):
    keys = re.findall(r'w+(\w+)\.' ,f)
    print (keys)
    return keys


def task_2 (f):
    ins = re.findall(r'<title>(\w+)(/w+)(\"\w+\".)(\d{4}-\d{2}-\d{2})</title>', f)
    return ins


def write_f(data, path, f):
    with open(path, 'w', encoding = 'utf-8') as file:
        path.write()
        
        #for key, value in dic.items():
        #   file.write(str(key)+'\t'+str(value)+'\n')
    return f
 
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerow(line)
    

def write_file(ins):
    with open(path, 'w', encoding = 'utf-8') as file:
        for phrase in ins:
            file.write(phrase[0]+' '+phrase[1]+' '+phrase[2]+'\t'+phrase[3]+'\t'+phrase[4]+' '+phrase[5]+'\n')
    return file
 
if __name__ == "__main__":
    f = read_f()
    data = ["doc_id".split(","), "title".split(","), "author".split(","), "created".split(","), "topic".split(","), "tagging".split(",")]    
    path = "output.csv"
    csv_writer(data, path)
    task(f)
    task_2(f)
    write_file(ins)
    print(file)

