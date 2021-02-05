from treat.treat import treatWord, treatFile

def openFile(name, path, option):
    file = open(path + name, option)
    return file


def openFiles(words, path):
    counter = 1
    while counter < 10:
        name = fileName(counter)
        file = openFile(name, path, 'r')
        words.append(treatFile(file))
        counter = counter + 1



def printFile(file):
    for line in file:
        print(line)


def createFile(name, path, content):
    file = open(path + name, 'w')
    for line in content:
        file.write(line + '\n')


def fileName(counter):
    if counter < 10:
        return 'legendas_0' + str(counter) + '.srt'
    return 'legendas_' + str(counter) + '.srt'


