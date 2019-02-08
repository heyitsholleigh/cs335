#!/usr/bin/python
import urllib


def wget(url):
    try:
        text = urllib.urlopen(url)
        if text.info().gettype() == 'text/html':
            print text.read()
    except IOError:
        print "Could not access we address ", url
        
        
wget('http://www.bounty.com/pregnancy-and-birth/baby-names/top-baby-names')        