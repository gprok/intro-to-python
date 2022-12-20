# Identify if a word is a palindrome

word = input("Give me a word: ")
mid = len(word) // 2

print(mid)

last = -1
is_palindrome = True

for i in range(mid):
    print(word[i], word[last])
    if word[i] != word[last]:
        is_palindrome = False
        break
    last = last - 1

if is_palindrome:
    print("It IS a palindrome")
else:
    print("NOT a palindrome")