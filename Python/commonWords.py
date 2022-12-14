# This is a program to find the top 10 most common words.
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

print('These are the Top 10 most common words:')
for val,key in lst[:10]:
    print(key,val)