import nltk

nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = """We are taking a simple example to display
stopword removal using NLTK"""

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []
for w in word_tokens:
    if w.lower() not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
