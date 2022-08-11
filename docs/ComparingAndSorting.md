# Comparing and Sorting Tuples

## Sorting Lists of Tuples

We can sort a list of tuples to get a sorted version of a dictinary. First we sort the dictionary by the key using the items() method and sorted() function.

```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> d.items()
dict_items([('a',10),('b',1),('c',22)])
sorted(d.items())
[('a',10),('b',1),('c',22)]
```

Another example:

```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = sorted(d.items())
>>> for k,v in sorted(d.items()):
>>>     print(k,v)
a 10
b 1
c 22
```

## Sort by values instead of key

If we could construct a list of tuples of the form (value,key) we colud sort by value. We do this with a for loop that creates a list of tuples.

```python
>>> c = {'a':10, 'c':22, 'b':1}
>>> tmp = list()
>>> for k,v in c.items():
>>>     tmp.append((v,k))
>>> print(tmp)
[(10,'a'),(22,'c'),(1,'b')]
>>> tmp = sorted(tmp, reverse=True)
>>> print(tmp)
[(22,'c'),(10,'a'),(1,'b')]
```
