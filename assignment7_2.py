fname = input('Please enter file name: ')
while True:
    try:
        fhand = open(fname)
        break
    except:
        fname = input("File not found, please try again: ")
        continue
query = "X-DSPAM-Confidence:"
total = 0
count = 0
#Class grading tool doesn't allow use of sum(), avoiding lists
for line in fhand:
    found = line.strip().find(query)
    if found == 0:
        sep = line.find(":")
        conf = float(line[sep+1:].strip()) #should use try/except due to possible error
        #print(conf, count)
        total = total + conf
        count = count + 1
average = total/(count)    
print("Average spam confidence:",average)