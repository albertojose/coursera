fname = input('Please enter file name: ')
while True:
    try:
        fhand = open(fname)
        break
    except:
        fname = input("File not found, please try again: ")
        continue
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
    for word in words:
        if not word in lst:
            lst.append(word)
        else:
            continue
lst.sort()
print(lst)