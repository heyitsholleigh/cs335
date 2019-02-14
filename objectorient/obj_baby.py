#!/usr/bin/python
import urllib
import re
import sys

class Babynames :
    def __init__(self, year):
        self.year = year


def main():
    args = sys.argv[1:]
    if not args:
       print 'usage: [--summaryfile] URL'
       sys.exit(1)
    
    summary = False
    if args[0] == '--summaryfile':
      summary = True
      del args[0]   
       
    
    try:
        text = urllib.urlopen(args[0])
        if text.info().gettype() == 'text/html':
            years = re.findall(r'\d+\sto\s\d+</h2><ul>(.*?)</ul>', text.read())
            for year in years:
                print year
            
            
            
    except IOError:
        print "Could not access web address "
        
    
if __name__ == '__main__':
  main()