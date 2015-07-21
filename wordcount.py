import csv

#open the document where info will be placed
handle = open('output.txt', "r")
text = handle.read()
words = text.split()
wordcount = 0

counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
    wordcount = wordcount + 1
    
print wordcount

with open('wordcount.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(counts.items())

