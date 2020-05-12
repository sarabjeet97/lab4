book = open("1342-0.txt")
words = open("word.txt")

book_words = book.read()
book_lower = book_words.lower()
book_list = book_lower.split()
book_set = set(book_list)

words_char = words.read()
words_lower = words_char.lower()
words_list = words_lower.split()
words_set = set(words_list)

c = 0

c = book_set.difference(words_set)
print(c)

