## Counting Words in Text
The general pattern that count the words in a line of text is to **split** the line into words, then loop through the words and use dictionary to track the count of each word independently.
```
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
```
## Definite Loops anf Dictionaries
Even though dictionaries are not stored in order, we can write a for loop that goes through all the **entries** in a dictionary and **looks up** the values.
```
counts = {'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
for key in counts:
    print(key,counts[key])
```
chuck 1
fred 42
jan 100

## Two Iteration Variables!
We loop through the **key-value** pairs in a dictionary using **two** iteration variables.
Each iteration, the first variable is the key and second variable is corresponding value of key.

August 8th 2022