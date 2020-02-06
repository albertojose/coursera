fname = input('Please enter file name: ')
while True:
    try:
        fhand = open(fname)
        break
    except:
        fname = input("File not found, please try again: ")
        continue
fh = open(fname)
query = 'From '
count = 0
for line in fh:
    if line.startswith(query):
        line = line.rstrip()
        lst = line.split()
        print(lst[1])
        count = count + 1
print('There were {} lines in the file with From as the first word'.format(count))