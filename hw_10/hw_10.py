import re
with open ("Popugai.html", "r", encoding="utf-8") as f:
    text = f.read()
result = re.findall(r'Отряд[^А-Я]+\w*', text)
res = re.search(r'\w*$', result[0])
with open("order.txt", "w", encoding="utf-8") as f:
    f.write("Отряд - ")
    f.write(res.group())
