text = input()

largest_word = ""
i = 0
word = ""

while text[i] != ".":
    if text[i] in "., ":
        if len(word) > len(largest_word):
            largest_word = word
            word = ""
    word += text[i]
    i += 1

k = len(largest_word)
i = 0
new_text = ""

while text[i] != ".":
    if text[i] in "., ":
        new_text += text[i]
    else:
        coded_elem = ord(text[i])
        coded_new_elem = coded_elem + k
        if 65 <= coded_elem <= 90 < coded_new_elem or 97 <= coded_elem <= 122 < coded_new_elem:
            new_text += chr(coded_new_elem - 26)
        else:
            new_text += chr(coded_new_elem)
    i += 1

new_text += "."

print(text)
print(new_text)
