def treatWords(words):
    treatedWords = []
    for line in words:
        for col in line:
            for word in col:
                word = treatWord(word)
                treatedWords.append(word.lower())
    return treatedWords



def treatWord(word):
    chars = ['<i>', '</i>', '.', ',', '?', '-', '"', '[', ']', '!']
    for char in chars:
        if char in word:
            word = word.replace(char, '')
    return word


def treatFile(file):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    words = []
    for line in file:
        aux = True
        for num in numbers:
            if str(num) in line or line == "\n":
                aux = False
                break
        if aux:
            words.append(line.split())
    return words

