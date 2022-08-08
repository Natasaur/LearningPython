#Count how many words are in the text.

counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

#print('Words: ',words)

numWords = 0

#Bulids a dictionary that counts how many times a word appears and counts
#the number of words at each iteration.
print('Counting... ')
for word in words:
    counts[word] = counts.get(word,0) + 1
    numWords = numWords + 1

print('Total of words:',numWords)