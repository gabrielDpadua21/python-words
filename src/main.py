from file.file import openFile, openFiles, printFile, createFile
from treat.treat import treatWord, treatFile, treatWords

words = []

openFiles(words, '../data/')

words = treatWords(words)

for word in words:
    print(word)



