import random
def read(txt):
    #эта функция считывает файл и возвращает случайный элемент
    #созданного массива
    with open(txt, encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        word = random.choice(words)
        return word

def imperative():
    #эта функция возвращает случайный глагол в повелительном наклонении;
    x = random.randint(1, 3)
    if x==1:
        txt="tu.txt"
    elif x==2:
        txt="nous.txt"
    elif x==3:
        txt="vous.txt"
    return read(txt)

def main_members(arg):
    #эта функция возвращает связанные между собой
    #артикль, существительное и глагол
    #В зависимости от аргумента глагол либо отрицательный, либо положительный,
    #либо в простом будующем времени(для условного предложения)
    verb = read("foundation.txt")  
    x = random.randint(1, 4)
    if x==1:
        noun="la " + read("la.txt")
    elif x==2:
        noun="l'" + read("l.txt")
    elif x==3:
        noun="le " + read("le.txt")
    if x==4:
        noun="les " + read("les.txt")
        if arg == "p":
            return noun + ' ' + verb + 'ent'
        elif arg == "n":
            if verb.startswith(("a", "e", "y", "u", "i", "o", "h")):
                return noun + " n'" + verb + 'ent pas'
            else:
                return noun + " ne " + verb + 'ent pas'
        elif arg == "c":
            verb = read("future.txt")+"ont"
            return noun + ' ' + verb
    else:
        if arg == "p":
            return noun + ' ' + verb + 'e'
        elif arg == "n":
            if verb.startswith(("a", "e", "y", "u", "i", "o", "h")):
                return noun + " n'" + verb + 'e pas'
            else:
                return noun + " ne " + verb + 'e pas'
        elif arg == "c":
            verb = read("future.txt")+"a"
            return noun + ' ' + verb

def noun():
    #эта функция возвращает случайное существительное с артиклем
    x = random.randint(1, 4)
    if x==1:
        noun="la " + read("la.txt")
    elif x==2:
        noun="l'" + read("l.txt")
    elif x==3:
        noun="le " + read("le.txt")
    elif x==4:
        noun="les " + read("les.txt")
    return noun

def place():
    #эта функция возвращает согласованные прилагательное,
    #существительное и предлог, обозначающие место
    y = random.randint(1, 2)
    x = random.randint(1, 2)
    if y==1:
        prep = "sur"
    elif y==2:
        prep = "dans"
    if x==1:
        place= prep+" la "+read("adjectives.txt")+ 'e ' + read("place_fem.txt")
    elif x==2:
        place= prep+" le "+read("adjectives.txt")+ ' ' + read("place_mas.txt")
    return place

def affirmatif():
    #эта функция возвращает утвердительное предложение
    affir ="L"+main_members("p")[1:]+' '+read("adverbs.txt") + ' ' + noun()+"."
    return affir

def interrogative():
    #эта функция возвращает вопросительное предложение
    x = random.randint(1, 4)
    if x==1:
        inter="Que "+read("foundation.txt")+"e "+noun()+' '+place()+"?"
    elif x==2:
        inter="Qui "+read("foundation.txt")+"e "+noun()+' '+place()+"?"
    elif x==3:
        inter="Quand "+main_members("p")+' '+noun()+' '+place()+"?"
    elif x==4:
        inter="Ou "+main_members("p")+' '+read("adverbs.txt")+' '+noun()+'?'
    return inter

def incitation():
    #эта функция возвращает побудительное предложение
    incit=imperative()+' '+read("adverbs.txt")+' '+noun()+'!'
    return incit

def negative():
    #эта функция возвращает отрицательное предложение
    x = random.randint(1, 2)
    if x==1:
        neg="Non, "+main_members("n")+' '+noun()+ ' ' + place() + '.'
    else:
        neg="L"+main_members("n")[1:]+' '+noun()+ ' ' + place() + '.'
    return neg

def conditionnelle():
    #эта функция возвращает условное предложение
    x = random.randint(1, 2)
    if x==1:
        cond="Si l"+affirmatif()[1:-1]+', '+main_members("c")+" la "
        cond+=read("adjectives.txt")+'e '+read("la.txt")+'.'
    elif x==2:
        cond="Si l"+affirmatif()[1:-1]+', '+main_members("c")+" le "
        cond+=read("adjectives.txt")+' '+read("le.txt")+'.'
    return cond

def main():    
    offres=[affirmatif(), interrogative(),
            incitation(), negative(), conditionnelle()]
    for i in range(5):
        i = random.choice(offres)
        print(i, end=' ')
        offres.remove(i)
main()
