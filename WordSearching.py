# word searching function. Just like ctrl + f (paste underneath text = f.read())

search_word = input("Enter the word you want to search: ")

if search_word in text:
    print()
    print(text.replace(search_word, '\033[44;33m{}\033[m'.format(search_word)))
else:
    print("Word not found")