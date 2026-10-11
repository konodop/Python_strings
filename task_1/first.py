original = input()

reverse_words = ""
reverse = ""
word = ""

for elem in original:
    reverse = elem + reverse
    word += elem

    if elem == " ":
        reverse_words = word + reverse_words
        word = ""

reverse_words = word + " " + reverse_words

print(reverse_words)
print(reverse)
