#Write the Program to implement stemming for a given sentence using NLTK 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
sentence = "Programmers program with programming languages"
words = word_tokenize(sentence)
stem_sentence = ""

for w in words:
    print(w, ":", ps.stem(w))
    stem_sentence += ps.stem(w) + " "

print("Original Sentence:", sentence)
print("Stem Sentence:", stem_sentence.strip())
