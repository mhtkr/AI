s = input("Enter the sentence: ")
wordlist = s.split(" ")
wordlist.sort()
print("Sorted words:")

for word in wordlist:
    print(word)
