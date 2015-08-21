from bs4 import BeautifulSoup
import urllib, urllib2

#function to encode parsed text
def encode(text):
    return text.encode('utf-8')

#input the query
#query = "besiege game"
query = raw_input("introduce query: ")

#open the document where links will be inserted
fout = open('links.txt', 'w')

#Function to get Google links for 10 first results 
def google_scrape(query):
    address = "http://www.google.com/search?q=%s&num=10&hl=en&start=0" % (urllib.quote_plus(query))
    request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urllib2.urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page)

    linkdictionary = {}

    for li in soup.findAll('h3', attrs={'class':'r'}):
        sLink = li.find('a')
        #print sLink['href']
        fout.write(sLink['href'] + '\n')
    return linkdictionary

if __name__ == '__main__':
    links = google_scrape(query)

#open the document where info will be placed
fout = open('output.txt', 'w')

#open list of urls to parse
fhand = open("links.txt")

lines = 0

#loop that gets the URL and extracts all textual content.
for line in fhand: 
    line = line.rstrip()
    try:
        soup = BeautifulSoup(urllib2.urlopen(line))
    except:
        continue
    for node in soup.findAll('p'):
        content = encode(''.join(node.findAll(text=True)))
        fout.write(content)
    lines = lines + 1

print "Processed lines:",lines
