text = str(input("Text: "))
words = {}
longest_word = ""
for word in text.split(" "):
    if word in words:
        words[word] += 1
    elif len(word) > len(longest_word):
        longest_word = word
        words[word] = 1
    elif word not in words:
        words[word] = 1
for key, value in sorted(words.items()):
    print("{:{}} : {}".format(key, len(longest_word), value))
