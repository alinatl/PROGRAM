print("Введите семь чисел через пробел")
a = list(map(int, input().split()))
with open("output.txt", "w", encoding="utf-8") as fout:
    for i in range(min(len(a), 7)):
        fout.write("X" * a[i] + '\n')


