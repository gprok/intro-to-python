# Count the number of words and letters in some text.
# Also find how many times letter 'a' appears in text

text = input("Give me some text: ")
words = text.split()

w = 0
c = 0
a = 0

for word in words:
    w += 1
    for ch in word:
        c += 1
        if ch == 'a':
            a += 1
    #c += len(word)

print("Words", w)
print("Words", len(words))
print("Chars", c)
print("A", a)
