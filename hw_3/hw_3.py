d=0
k=0
word=input("Введите вашу строку")
f=len(list(word))
while d<f:  
    for w in word:
        print(word[d:])
        d+=1
        word_1=list(word)
        a=word[0]
        word_1.remove(a)
        word_2=word
input()
        
