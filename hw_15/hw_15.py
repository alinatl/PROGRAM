import re
punctuation = ('-', ',', ';', ':', '(', ')', '"')

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()
sentences = re.findall('[^.!?]+', text)

for sentence in sentences:
    for i in punctuation:
        sentence = sentence.replace(i , '')
    if len(sentence.split()) >= 10:
        length = [len(word) for word in sentence.split()]
        average = 0
        for i in length:
            average+=i
        average/=len(sentence.split())
        print("Это предложение со словами длины {:.1f}".format(average))
