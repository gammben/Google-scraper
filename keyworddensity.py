import csv
from nltk.corpus import stopwords
#open the document where info will be placed
handle = open('output.txt', "r")
text = handle.read()
lowertext = text.lower()


#remove commas and other signs
cleantext = "".join(c for c in lowertext if c not in ('!','.',':',',',';'))

#Split text in words
words = cleantext.split()

#Filter omit words in text
filtered_words = [word for word in words if word not in stopwords.words('english')]

wordcount = 0   
counts = dict()
for word in filtered_words:
    counts[word] = counts.get(word,0) + 1
    wordcount = wordcount + 1

print wordcount

with open('wordcount.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(counts.items())
   
fout = open('wordcount-2.txt', 'w')
     
for i in range(len(filtered_words)-1):
    twowords = [filtered_words[i], filtered_words[i+1]]
    twostring = str(twowords)
    fout.write(twostring + '\n')
    
fout = open('wordcount-3.txt', 'w')
     
for i in range(len(filtered_words)-1):
    triplets = [filtered_words[i], filtered_words[i+1], filtered_words[i+2]]
    threestring = str(triplets)
    fout.write(threestring + '\n')