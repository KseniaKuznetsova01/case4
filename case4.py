""" Case-study #3 Investment report
Developers:

Panukova E. (65%) , Kuznetsova K. (70%)

"""
from textblob import TextBlob
import local as lc
text = input(lc.TEXT)
text = text.lower()
text1 = text
number_s = 0
number_w = 1
sentence = text.find('.')
while sentence != -1:
    number_s += 1
    text1 = text1[sentence+1:]
    sentence = text1.find('.')
print(lc.SENTENCE, number_s)
text1 = text
words = text.find(' ')
while words != -1:
    number_w += 1
    text1 = text1[words+1:]
    words = text1.find(' ')
print(lc.WORDS, number_w)
syllables = 0
number = len(text)
for i in text:
    if i == 'а' or i == 'у' or i == 'е' or i == 'о' or i == 'ю' or i == 'и' \
            or i == 'я' or i == 'э' or i == 'ё' or i == 'ы':
        syllables += 1

print(lc.SYLLABLES, syllables)

number_asl = number_w / number_s
print(lc.ASENTENCE, number_asl)
number_asw = syllables / number_w
print(lc.ASYLLABLES, number_asw)

number_fre_russ = 206.835 - (1.3 * number_asl) - (60.1 * number_asw)
number_fre_enl = 206.835 - (1.015 * number_asl) - (84.6 * number_asw)

print(lc.FRE, number_fre_russ)
if number_fre_russ <= 25:
    print(lc.HARD)
elif 25 < number_fre_russ <= 50:
    print(lc.M_HARD)
elif 50 < number_fre_russ <= 80:
    print(lc.M_EASY)
else:
    print(lc.EASY)
