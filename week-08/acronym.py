# Read a sentence from the user and produce the acronym
# using the first letter of each word

sentence = input("Give a sentence:")
words = sentence.split()

acronym = ''
for word in words:
    # acronym = acronym + word[0]
    acronym += word[0]

print(acronym)
