def read(txt):
    #эта функция считывает файл с текстом и возвращает список слов
    with open(txt, encoding="utf-8") as f:
        text = f.read()
    punctuation = ('-', ',', '.', ';', ':', '(', ')', '"', '?', '!')
    for i in punctuation:
        text = text.replace(i , '')
    text = text.lower()
    words = text.split()
    return words

def omni_freq(words):
    #эта функция считывает количество слов, начинающихся с "omni"
    #и возвращат частотный словарь
    omni = {}
    for word in words:
        if word.startswith('omni'):
            if word in omni:
                omni[word] += 1
            else:
                omni[word] = 1
    return omni

def without_omni_freq(words, omni):
    #эта функция считывает количество слов без приставки "omni"
    #и возвращает частотный словарь
    without_omni = {}
    for word in omni:
        if word[4:] in words:
                for word_1 in words:
                    if word_1 == word[4:]:
                        if word_1 in without_omni:
                            without_omni[word_1] += 1
                        else:
                            without_omni[word_1] = 1
    return without_omni
    
def print_freq(dictionary):
    #эта функция выводит на экран все ключи и значения словаря
    for word, amount in dictionary.items():
        print('\t', word, "—", amount)
    if len(dictionary) == 0:
        print('\tThere are no words')

def main():
    omni = omni_freq(read("text.txt"))
    without_omni = without_omni_freq(read("text.txt"), omni)

    print('Words starts with the prefix "omni":')
    print_freq(omni)
    print('Words without the prefix "omni":')
    print_freq(without_omni)
    
main()
