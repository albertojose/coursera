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
senders = dict()
for line in fh:
    if line.startswith(query):
        words = line.rstrip()
        lst = words.split()
        senders[lst[1]] = senders.get(lst[1],0)+1
bigcount = None
bigsender = None
for sender,count in senders.items():
    if bigcount is None or count > bigcount:
        bigsender = sender
        bigcount = count
print(bigsender,bigcount)