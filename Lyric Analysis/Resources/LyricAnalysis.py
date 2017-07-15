#Benjamin Shelton
#Extra-Curricular Program 1: Lyric Analysis
#This Program (So far) reads in lyrics of songs from text files
#and counts the total number of times each word in the song is used.
#It also takes that data and creates an excel workbook that has a worksheet
#for every song and the associated word count with it
import sys,os
import collections
import string
import glob
import pprint as pp
import xlsxwriter

#gets the different genre folders
def getFolderList(DIRPATH):

    folderList = os.listdir(DIRPATH)
    folderList.remove('Resources')
    return folderList

#gets the number of times each word is said and then cuts off
#any words said less than the frequency
def getFrequentWords(lyrics, frequency):

    punct = ['!', '#', '"', '%', '$', '&', ')', '(', '+', '*', '-', "'", ',', '.', '?']
    articles =['A', 'An', 'And', 'The']

    songWords = {}
    printList = []

    for word in lyrics.split():
        for char in punct:
            word = word.replace(char, '')

        word = word.lower()
        word = word.title()

        for article in articles:
            if word == article:
                word = ''
        
        if word != '':
            if not word in songWords:
                songWords[word] = 1
            else:
                songWords[word] += 1

    songWords = sorted(songWords.items(), key=lambda kv: kv[1], reverse=True)

    for word in songWords:
        if word[1] > frequency:
            printList.append(word)
    
    return printList

#gets the percentage of each word
def getPercentageList(lyricList):
    #total number of words in list
    total = 0
    percList = []

    for word in lyricList:
        total += word[1]
    
    for word in lyricList:
        perc = word[1] / total
        percList.append((word[0], "{:.1%}".format(perc)))

    return percList



def makeExcelSheet(folder, DIRPATH):

    workbook = xlsxwriter.Workbook(DIRPATH + '\\Resources\\Excel Files\\' + folder + '.xlsx')
    pieChart = workbook.add_chart({'type': 'pie'})

    for filename in glob.glob(os.path.join(DIRPATH + '\\' + folder, '*.txt')):
        f = open(filename, 'r')
        lyrics = f.read()
        proxyLyrics = lyrics
        lyrics = getFrequentWords(lyrics, 0)

        excelName = filename.replace(DIRPATH + '\\' + folder + '\\', '')
        excelName = excelName.replace('.txt', '')

        if len(excelName) > 31:
            excelName = ''.join(excelName.partition('by')[:2])
            excelName.replace('by', '')

        worksheet = workbook.add_worksheet(excelName)

        wordList = []
        numOfOccurences = []
        
        for k in lyrics:
            wordList.append(k[0])
            numOfOccurences.append(k[1])

        worksheet.write_column('A1', wordList)
        worksheet.write_column('B1', numOfOccurences)

        percList = getPercentageList(lyrics)

        proxyLyrics = getFrequentWords(proxyLyrics, 5)
        strippedList = []

        percTotal = 0
        percDeficit = 100

        for x in range(len(proxyLyrics)):
            stripped = percList[x][1].replace('%', '')
            stripped = float(stripped)
            strippedList.append(stripped)

            wordList = percList[x][0]
            percTotal += stripped
        
        percDeficit = percDeficit - percTotal
        strippedList.append(percDeficit)

        data = [
            [wordList],
            [strippedList]
        ]

        pieChart.add_series({
            'categories': data[0],
            'values': data[1]
        })

        worksheet.insert_chart('C1', pieChart)
    workbook.close()
        
            

        


#prints the words to the console
def printWordReport(folder, DIRPATH):
    print(folder)
    print('---------------------------------------------------------------------------------------------------------------------------')
    for filename in glob.glob(os.path.join(DIRPATH + '\\' + folder, '*.txt')):
        f = open(filename, 'r')
        printName = filename.replace(DIRPATH + '\\' + folder + '\\', '')
        printName = printName.replace('.txt', '')

        lyrics = f.read()
        printList = getFrequentWords(lyrics, 5)
        
        print(printName)
        print(printList)
        print()


#Do not call this function if you are calling printWordReport
def outfileWordReport(folder, DIRPATH):

    sys.stdout = open(DIRPATH + '\\Resources\\Outfiles\\' + folder + '.txt', "w")

    printList = []

    print(folder)
    print('---------------------------------------------------------------------------------------------------------------------------')
    for filename in glob.glob(os.path.join(DIRPATH + '\\' + folder, '*.txt')):
        f = open(filename, 'r')
        printName = filename.replace(DIRPATH + '\\' + folder + '\\', '')
        printName = printName.replace('.txt', '')

        lyrics = f.read()
        printList = getFrequentWords(lyrics, 5)
        
        print(printName)
        print(printList)
        print()


if __name__ == '__main__':

    DIRPATH = os.path.dirname(os.path.realpath(__file__)) + '\\..'

    folderList = getFolderList(DIRPATH)

    for folder in folderList:
        #printWordReport(folder, DIRPATH)
        #outfileWordReport(folder, DIRPATH)
        makeExcelSheet(folder, DIRPATH)
            
