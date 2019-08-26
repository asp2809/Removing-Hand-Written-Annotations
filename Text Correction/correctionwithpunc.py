# Program to correct the text using PySpellChecker and dictionary with Punctuations
import os
import re
from spellchecker import SpellChecker

os.system("tesseract inpaint.png ocrout")

with open('ocrout.txt', 'r') as file:
    data = file.read().replace('\n', '')

print(data)

spell = SpellChecker()

sentenceArray=data.split(" ")

puncRegex = "[.!?,:;]"

wordPuncDict = []

for wordWithPunc in sentenceArray:
    punc = re.search(puncRegex, wordWithPunc)
    wordWithPuncObj = {}
    wordWithPuncObj["word"] = wordWithPunc
    if punc != None:
        wordWithPuncObj["punc"] = punc.group()
    wordPuncDict.append(wordWithPuncObj)

for word in wordPuncDict:
    temp = spell.correction(word["word"])
    if "punc" in word:
        temp+=word["punc"]
    word["correct"] = temp

res = " ".join([x["correct"] for x in wordPuncDict])

print(res)

file = open("result.txt", "w")
file.write(res)
file.close()