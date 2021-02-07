from file.file import openFile, openFiles, printFile, createFile, appendFile
from treat.treat import treatWord, treatFile, treatWords

words = []

openFiles(words, '../data/')

words = treatWords(words)

wordsDic = {}

for word in words:
    if word in wordsDic:
        wordsDic[word] += 1
    else:
        wordsDic[word] = 1

createFile('words.txt', '../data/', '')

for word in wordsDic:
    line = 'Word: ' + word + ' - Used: ' + str(wordsDic[word])
    appendFile(line, '../data/', 'words.txt')



