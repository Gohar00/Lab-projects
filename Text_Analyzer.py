txt = ""
symbols = "'.,!?><@#$%^&*()"

# 1. opening a file and passing the data in it to a string "txt"
with open("date.txt", encoding='utf-8') as f:
    for line in f:
        txt = txt + line
# 2. converting all letters lowercase
txt = txt.lower()

# 3. count of the sentences
sentence_count = sum(1 for s in txt if s in '.!?')

# 4. count of the words(without special characters)
word_count = sum(1 for w in txt if w in ' \n\t,')

# 5. the count of the word which is the most used in the text
for i in txt:
    if i in symbols:
        txt = txt.replace(i, "")
max_count_word = max((txt.count(el), el) for el in txt.split())

# 6. the count of the letters
txt = txt.replace(" ", "")
letters_count = len(txt)

# 7. the count of the letter which is the most used in the text
max_count_letter = max((txt.count(l), l) for l in txt)

# 8. opening second file and adding the dates
with open("date2.txt", 'w') as f2:
    f2.write(f'1. WORDS: {word_count}\n'
             f'2. SENTENCES: {sentence_count}\n'
             f'3. LETTERS: {letters_count}\n'
             f'4. LETTER FREQUANCY: {max_count_letter}\n'
             f'5. WORD FREQUANCY: {max_count_word}')
