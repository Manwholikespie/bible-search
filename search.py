# John 17:3
# Romans 5:10
# Romans 12:1-2
# Ephesians 1:7
# Eph 2:8-9
# 1 Peter 2:15
# 1 Peter 5:7

import bible
import requests
from bs4 import BeautifulSoup

"http://www.biblestudytools.com/nas/john/17-3.html"

def getRef(searchStr):
    if '-' not in searchStr:
        v = bible.Verse(searchStr)
        return v

    else:
        v1 = bible.Verse(searchStr)

        endingVerse = searchStr.rsplit("-",1)[1]
        newSearchStr = v1.format("B C") + ":" + endingVerse
        v2 = bible.Verse(newSearchStr)

        p = bible.Passage(v1,v2)
        return p

def cleanText(inputStr):
    # take the numbers, line returns, and quotes out of the text
    cleanedText = ''.join([i for i in inputStr if not i.isdigit()]).replace(
        "\n","").replace('"','').replace("\t","").replace("\r","").replace("  ","")

    return cleanedText

def searchVerse(searchStr):
    # Pull info from the reference we are searching for
    ref = getRef(searchStr)
    book = ref.format("B").replace(" ","-")
    chapter = ref.format("C")
    if '-' in ref.format():
        verses = ref.format("V-v")
        passageLength = (ref.end.verse - ref.start.verse) + 1
    else:
        verses = int(ref.format("v"))
        passageLength = 1

    # Get the URL of the bible verse
    chapter = str(chapter)
    url = "http://www.biblestudytools.com/nas/" + book + "/"
    if type(verses) is str:
        url += "passage/?q="
        url += book + "+" + chapter + ":" + verses
    else:
        verses = str(verses)
        url += chapter + "-" + verses + ".html"

    # print(url)
    """
    either:

    mult:    http://www.biblestudytools.com/nas/john/passage/?q=john+17:3-5
    or
    single:  http://www.biblestudytools.com/nas/john/17-3.html
    """

    # Set up the soup of beauty
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    passage = ""

    # parse the page for the text
    if passageLength > 1:
        for x in xrange(ref.start.verse, ref.end.verse+1):
            verseText = [item.text for item in soup.select("span.verse-"+str(x))][0]
            passage += " " + cleanText(verseText)
    else:
        verseText = [item.text for item in soup.select("span.verse-"+str(verses))][0]
        passage += " " + cleanText(verseText)

    print passage

# searchVerse("John",17,3)

verses = [
'John 17:3',
'Romans 5:10',
'Romans 12:1-2',
'Ephesians 1:7',
'Eph 2:8-9',
'1 Peter 2:15',
'1 Peter 5:7'
]

for verse in verses:
    searchVerse(verse)
