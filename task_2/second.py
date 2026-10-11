text = input()

largest_word = ""
i = 0
word = ""

while text[i] != ".":

    if text[i] in "., ":

        if 21 > len(word) > len(largest_word):
            largest_word = word
        word = ""

    else:
        word += text[i]
    i += 1

k = len(largest_word)
i = 0
new_text = ""

while text[i] != ".":

    if text[i] not in "., ":
        new_text += text[i]
    else:
        coded_elem = ord(text[i])
        coded_new_elem = coded_elem + k

        if (65 <= coded_elem <= 90 < coded_new_elem
                or 97 <= coded_elem <= 122 < coded_new_elem):
            coded_new_elem = coded_new_elem - 26

        new_text += chr(coded_new_elem)

    i += 1

new_text += "."

print(k)
print(new_text)
