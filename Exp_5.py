import string

def remPunc(text):
    punc = string.punctuation
    table = str.maketrans("", "", punc)
    return text.translate(table)

text = input("Enter the string with punctuations: ")
new_text = remPunc(text)
print("String without punctuations:", new_text)
