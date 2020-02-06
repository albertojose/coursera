fname = input('Please enter file name: ')
while True:
    try:
        fhand = open(fname)
        break
    except:
        #fname = input("File not found, please try again: ")
        fname = 'mbox-short.txt'
        continue
fh = open(fname)
query = 'From '
hours = dict()
for line in fh:
    if line.startswith(query):
        words = line.rstrip()
        lst = words.split()
        time = lst[5].split(':')
        hours[time[0]] = hours.get(time[0],0)+1
for k,v in sorted(hours.items()):
    print(k,v)