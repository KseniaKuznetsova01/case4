""" Case-study #3 Investment report
Developers:

Panukova E. (65%) , Kuznetsova K. (70%)

"""
from textblob import TextBlob                            # Imports the module TextBlob.
import local as lc                                       # Imports the module Local.


text2 = input(lc.TEXT)
text = text2.lower()                                     # Lowercase translation of the entered text.
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
english = 0
russian = 0

for i in text:
    if i == 'а' or i == 'у' or i == 'е' or i == 'о' or i == 'ю' or i == 'и' \
            or i == 'я' or i == 'э' or i == 'ё' or i == 'ы':
        syllables += 1
        russian += 1

    elif i == 'e' or i == 'y' or i == 'u' or i == 'i' or i == 'o' or i == 'a':
        syllables += 1
        english += 1

print(lc.SYLLABLES, syllables)

number_asl = number_w / number_s                         # The calculation of the index of ASL.
print(lc.ASENTENCE, number_asl)
number_asw = syllables / number_w                        # The calculation of the index of ASW.
print(lc.ASYLLABLES, number_asw)

number_fre_text = 0
if english == 0:
    number_fre_text = 206.835 - (1.3 * number_asl) - (60.1 * number_asw)     # The calculation of the index of Flesh.
    print(lc.FRE, number_fre_text)

    if number_fre_text <= 25:
        print(lc.HARD)
    elif 25 < number_fre_text <= 50:
        print(lc.M_HARD)
    elif 50 < number_fre_text <= 80:
        print(lc.M_EASY)
    else:
        print(lc.EASY)

    polarity_1 = TextBlob(text2)
    polarity = polarity_1.sentiment                              # Returns the subjectivity score.
    polarity_2 = int(polarity[0])
    subjectivity = int(polarity[1])

    if polarity_2 < 0:
        print(lc.NEGATIVITY)
    elif polarity_2 == 0:
        print(lc.NONE)
    elif polarity_2 > 0:
        print(lc.POSITIVITY)

else:
    number_fre_text = 206.835 - (1.015 * number_asl) - (84.6 * number_asw)
    print(lc.FRE, number_fre_text)

    if number_fre_text <= 25:
        print(lc.HARD)
    elif 25 < number_fre_text <= 50:
        print(lc.M_HARD)
    elif 50 < number_fre_text <= 80:
        print(lc.M_EASY)
    else:
        print(lc.EASY)

    polarity_1 = TextBlob(text2)
    polarity = polarity_1.sentiment                                  # Returns the subjectivity score.
    polarity_2 = int(polarity[0])
    subjectivity = int(polarity[1])

    if polarity_2 < 0:
        print(lc.NEGATIVITY)
    elif polarity_2 == 0:
        print(lc.NONE)
    elif polarity_2 > 0:
        print(lc.POSITIVITY)

    print(lc.OBJECTIVITY, '{}%'.format(subjectivity))


