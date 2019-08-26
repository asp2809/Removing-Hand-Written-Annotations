# from pattern.en import suggest
import os
import re
from autocorrect import spell

# os.system("tesseract inpaint.png out")

with open('out.txt', 'r') as file:
    data = file.read().replace('\n', '')

sentenceArray=[]

for word in data.split(" "):
    sentenceArray.append(spell(word))

print(" ".join(sentenceArray))


# def reduce_lengthening(text):
#     pattern = re.compile(r"(.)\1{2,}")
#     return pattern.sub(r"\1\1", text)


# word = "amazzziiing"
# word_wlf = reduce_lengthening(word) #calling function defined above
# print(word_wlf) #word lengthening isn't being able to fix it completely

# correct_word = suggest(word_wlf) 
# print(correct_word)