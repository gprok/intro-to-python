import random

words = ["mississippi", "polymorphism", "empathy", "television", "internet"]

pos = random.randint(0, len(words)-1)

print(pos, words[pos])

w = words[pos]
secret = w[0]
for i in range(len(w)-2):
    secret = secret + '_'
secret = secret + w[-1]

print("Secret", secret)
