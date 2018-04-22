import os
file_list = os.listdir()
files = []
punctuation = ('-', ',', '.', ';', ':', '(', ')', '"', '?', '!')

def name(string):
    k=1
    for j in reversed(string):
        if j != '.':
            k+=1
        else:
            string = string[:len(string)-k]
            return string

print("Files with puctuation:")
for file in file_list:
    if os.path.isfile(file):
        file = name(file)
        for i in punctuation:
            if i in file:
                print(file)
                files.append(file)
                break
print("\nOther files and directories: ")
for file in file_list:
    if os.path.isfile(file):
        file = name(file)
    if file not in files:
        if file != None:
            files.append(file)
            print(file)

            
