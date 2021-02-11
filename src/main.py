import csv
from file.file import openFile, openFiles, printFile, createFile, appendFile
from treat.treat import treatWord, treatFile, treatWords
import pandas as pd

words = []

openFiles(words, '../data/')

words = treatWords(words)

wordsDic = {}

for word in words:
    if word in wordsDic:
        wordsDic[word] += 1
    else:
        wordsDic[word] = 1

createFile('words.csv', '../data/', '')

with open('../data/words.csv', 'w') as data:
    writer = csv.writer(data)
    writer.writerow(('Word', 'Usage'))
    for word in wordsDic:
        writer.writerow((word, wordsDic[word]))


table = pd.read_csv('../data/words.csv')

print(table.tail(100))


    


