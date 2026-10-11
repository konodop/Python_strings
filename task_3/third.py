text = input()

ru_low = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ru_high = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
en_low = "abcdefghijklmnopqrstuvwxyz"
en_high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = ru_low + ru_high + en_low + en_high

words = {}
buffer = ""

for elem in text:

    if elem in letters:
        buffer += elem

    elif buffer:
        word = words.get(buffer)

        if not word:
            words[buffer] = 1
        else:
            words.update({buffer: word + 1})

        buffer = ""

top = (sorted(words.items(), key=lambda x: x[1], reverse=True))

print("Пять самых встречающихся слов:", *top[:5])
