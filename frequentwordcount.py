name = input('Enter file: ')
# fhandle = open('test.txt')

counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
mostfrequentword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        mostfrequentword = word
        bigcount = count

print(mostfrequentword, bigcount)
