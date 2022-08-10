# Tuples

These are like lists.  
Tuples are ampther kind of sequence that functions much like a list. They have elements which are indexed starting at 0.

```bash
x = ('Glenn','Sally','Joseph')
print(x[2])
```

This prints the name "Joseph".

```bash
y = (1,9,2)
for iter in y:
    print(iter)
```

This prints:
1  
9  
2  
  
  Unlike a list, once you create a **tuple**, yo cannot alter its contents.  
  
  ```bash
  This is the example of modifing a list:
  x = [9,8,71]
  x[2] = 6
  print(x)

  [9,8,6]
  ```

  ```bash
  This is the example of modifing a tuple:
  y = 'ABC'
  y[1] = 'D'
  **Error message**
  ```

## Tuples are more efficient

Since Python does not have to build tuple structures to be modifiable, they are simplier and more efficient in terms of memory use and performance than lists.  
## Tuples and Assignment

We can put a tuple on the **left-hand sided** of an assignment statement.  

```bash
>>>(x,y) = (4,'freud')
>>>print(y)
freud
>>>print(x)
4
```

## Tuples and Dictionaries

The items() method in dictionaries returns a list of (key,value) tuples.

```bash
>>>d = dict()
>>>d['cewn'] = 2
>>>d['csev'] = 4
>>>for (k,v) in d.items():
>>>     print(k,v)
cwen 2
csev 4
```

