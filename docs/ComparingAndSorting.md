# Sorting Lists of Tuples

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

