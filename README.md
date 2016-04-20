#Bible-Search
Greetings, and welcome to another simple scraping script by yours truly. This one is fairly simple to use, as you can just modify the search.py file as needed. Eventually I'll add something where you can just write down the references you want in another file, and it will spit out the text in another file, but I didn't really feel like adding all of that right now. Anyways, let's talk about installing it.

##Installation
### Depdendencies
- The [bible module](https://github.com/jasford/python-bible).  
- [Requests](http://docs.python-requests.org/en/master/).  
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).  

To install these dependencies, do as I do...  

```fish
 ⚓  ~/D/P/bible  master ⚑  pip install bible  
 ⚓  ~/D/P/bible  master ⚑  pip install requests  
 ⚓  ~/D/P/bible  master ⚑  pip install beautifulsoup4  
```

and you're done!

## Special Thanks
To [biblestudytools](http://biblestudytools.com). I really like the way that you guys lay out your information, and the way you designed your URL layout. I would have prefered to use [biblegateway](https://www.biblegateway.com), as they allowed for an easy way to remove the verse numbers, footnote characters, etc.— However, they store all of these special settings within giant cookies. Giant 1.4KB, 1350+ character long cookies.