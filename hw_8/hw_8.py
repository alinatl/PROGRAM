import random
d = {}
list_d = []
def read():
    #функция читает файл и делает из него словарь
    with open('text.csv') as f:
        for line in f:
            line = line.replace('\n', '')
            key, word= line.split(';', maxsplit=1)
            dict_list = d.setdefault(key, word)
            list_d.append(key)
            word = ''
            
r_choice = ''
def choice():
    global r_choice
    #функция случайно выбирает одно из слов
    r_choice = random.choice(list_d)

def question(r_choice):
    #спрашивает, ищет подходящее слово, сравнивает
    vvod = input('введите сущ. наиболее употребимое со словом '+r_choice+'...')
    vvod = vvod.lower()
    if vvod == str(d[r_choice]):
        return True
    else:
        return False


def main():
    read()
    choice()
    count = 3
    while count!=0:
        if question(r_choice) == True:
            print('ура! вы угадали! Победа')
            break
        else:
            count-=1
            print('неверный ответ!')
            if count>0:
                print('Попробуй еще разок. У тебя'+'\n'+'осталось попыток: '+str(count))
            else:
                print('попытки закончились, вы проиграли. Вот так выглядит ПОРАЖЕНИЕ')
               
main()
input()

