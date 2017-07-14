#Benjamin Shelton
#Extra-Curricular Program 1: Lyric Analysis
#This Program (So far) reads in lyrics of songs from text files
#and counts the total number of times each word in the song is used.
#

import sys,os
import collections
import string
import glob
import pprint as pp
import xlsxwriter

def getFolderList(DIRPATH):

    folderList = os.listdir(DIRPATH)
    folderList.remove('Resources')
    folderList.remove('Excel Files')
    return folderList

def getFrequentWords(lyrics, frequency):

    punct = ['!', '#', '"', '%', '$', '&', ')', '(', '+', '*', '-', "'", ',', '.', '?']

    songWords = {}
    printList = []

    for word in lyrics.split():
        for char in punct:
            word = word.replace(char, '')
        word = word.lower()
        word = word.title()
        if not word in songWords:
            songWords[word] = 1
        else:
            songWords[word] += 1

    songWords = sorted(songWords.items(), key=lambda kv: kv[1], reverse=True)

    for word in songWords:
        if word[1] > frequency:
            printList.append(word)
    
    return printList

def makeExcelSheet(folder, DIRPATH):
    pass

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

if __name__ == '__main__':

    DIRPATH = os.path.dirname(os.path.realpath(__file__)) + '/..'

    folderList = getFolderList(DIRPATH)

    for folder in folderList:
        printWordReport(folder, DIRPATH)
        # print(folder)
        # print('---------------------------------------------------------------------------------------------------------------------------')
        # for filename in glob.glob(os.path.join(DIRPATH + '\\' + folder, '*.txt')):
        #     f = open(filename, 'r')
        #     printName = filename.replace(DIRPATH + '\\' + folder + '\\', '')
        #     printName = printName.replace('.txt', '')

        #     lyrics = f.read()
        #     printList = getFrequentWords(lyrics, 5)
            
        #     print(printName)
        #     print(printList)
        #     print()
            
