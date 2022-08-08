#This is a program that counts the times a 
#name appears in a list using the get() method

counts = dict()
names = ['csev','cwen','csev','zquian','cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)