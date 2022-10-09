def compress(text):

    """This function compresses the text."""
    compressed = ''
    count = 1

    # 1. checks if the count of the letter, and if the letter is repeated, writes it once and adds the number of repetitions
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            count += 1
        else:
            compressed = compressed + text[i] + str(count)
            count = 1
    compressed = compressed + text[i+1] + str(count)
    return compressed

def decompress(text):

    """This function decompresses the text."""
    decompressed = ''

    # 2. checks the count of the letter and adds that letter so many times
    for i in range(1, len(text), 2):
        count = int(text[i])
        decompressed = decompressed + (text[i - 1] * count)
    return decompressed


while True:

    # 3. gives a question and suggest options
    question_1 = input("What option you want?\nPress c(if you want compress the text) or d(for decompress): ")

    if question_1 == 'c':
        text = input("Enter your text please: ")
        print(f'The compressed text is: {compress(text)}')
    elif question_1 == 'd':
        text = input("Enter your text please: ")
        print(f'The decompressed text is: {decompress(text)}')
    else:
        print("Please enter 'c' or 'd'")

    # gives second question for continue the operation
    question_2 = input("Do you want finish the operation? y/n : ")
    if question_2 == 'n':
        continue
    elif question_2 == 'y':
        break



