import local as lc
text = input(lc.TEXT)
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
syllables = 1
number = len(text)
for i in text:
    if i == 'а' or i == 'у' or i == 'е' or i == 'о' or i == 'ю' or i == 'и' \
            or i == 'я' or i == 'э' or i == 'ё' or i == 'ы':
        syllables += 1

print(lc.SYLLABLES, syllables)

number_asl = number_w / number_s
print(lc.ASENTENCE, '{:.3f}'.format(number_asl))
number_asw = syllables / number_w
print(lc.ASYLLABLES, '{:.3f}'.format(number_asw))

number_fre = 206.835 - (1.3 * number_asl) - (60.1 * number_asw)
fre = '{:.4f}'.format(number_fre)
print(lc.FRE, fre)
if fre <= 25:
    print(lc.HARD)
elif 25 < fre <= 50:
    print(lc.M_HARD)
elif 50 < fre <= 80:
    print(lc.M_EASY)
else:
    print(lc.EASY)