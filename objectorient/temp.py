#!/usr/bin/python
import urllib
import re
import sys

class Babynames :
    def __init__(self, year):
        self.year = year
        self.names = names
        
    def retrieveNames(self, url) :
        #create method to get the names
        #self.names = result
        names = {}
        
    def printNames(self) :
        print self.names
        #iterate through self.names and print list
 

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
                #extract URL from <li> tag and add URL to list
            #instantiate my objects for getting baby names
            #iterate through list of URLs from above
               for yearURL in yearURLs:
                   bn = Babynames(yearURL)
                   bn.printNames()
            
            
            
    except IOError:
        print "Could not access web address "
        
    
if __name__ == '__main__':
  main()