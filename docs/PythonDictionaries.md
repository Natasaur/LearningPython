## What's a collection?
We can put more than one value in it and carry them all around in one convenient package.
    **- List:** A linear collection of values that stay in order.
    **- Dictionary:** A bag of values, each with its own label. Dictionaries are Python's most pwerful data collection, they allow us to do data based-like operations in Python.

## Making Histograms
One common use of dictionaries is counting how often we see something. It is an error to reference a key which is not in the dictionary.
**We can use the "in" operator to see if a key is in the dictionary.**

When we encounter a new name, we need to add a new entry in the dictionary and if this is the second or later time it appears, we simply add one to the count in the dictionary under the name.
```
counts = dict()
names = ['csev','cwen','csev','zquian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
        else:
            counts[name] = counts[name] + 1
print(counts)
```
### Simplified counting with get()
We can use get() and provide a default value zero when the key is not yet in the dictionary and then just add it.
The pattern of checking to see if a key is already in the dictionary and assuming a default value if the key is not there is so common that there is a mthod called get()that does that for us.
```
counts = dict()
names = ['csev','cwen','csev','zquian','cwen']
for name in names:
        counts[name] = counts.get(name,0) + 1
print(counts)
```
August 8th 2022