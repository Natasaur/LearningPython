#This is a program that counts the times a 
#name appears in a list the old schoool way#

counts = dict()
names = ['csev','cwen','csev','zquian','cwen']
for name in names:
    if name not in counts :
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)