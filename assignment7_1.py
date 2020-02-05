fname = input('Please enter file name: ')
while True:
    try:
        fhand = open(fname)
        break
    except:
        fname = input("File not found, please try again: ")
        fhand = open(fname)
        continue
for line in fhand:
    print(line.rstrip().upper())
