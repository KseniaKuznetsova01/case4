import local as lc
text = input(lc.TEXT)
text1 = text
number_s= 0
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
syllables = 1
number = len(text)
for i in text:
    if i == 'а' or i == 'у' or i == 'е' or i == 'о' or i == 'ю' or i == 'и' or i == 'я' or i == 'э' or i == 'ё' or i == 'ы':
        syllables += 1
print(lc.SYLLABLES, syllables)