#!/usr/bin/python
import urllib
import re
import sys

d = {}

class Babynames :
    def __init__(self, year):
        self.year = year
        self.d = d
        
    def retrieveNames(self, tuples) :
        #create method to get the names
        #self.names = result
        #d = {}
        
        for tuple in tuples:
          (rank, boy, girl) = tuple
          if boy not in d:
            d[boy] = rank
          if girl not in d:
            d[girl] = rank
            
        
        
    def printNames(self, d) :
        print self.d
        #iterate through self.names and print list
        #for name in self.d:
         #   print(name)
 

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
              tuples = re.findall(r'<li>(.*?)</li>', text.read())
              for tuple in tuples:
                 bn = Babynames(tuple) 
                 bn.retrieveNames(tuple)
                 bn.printNames()
            #extract URL from <li> tag and add URL to list 
            #instantiate my objects for getting baby names
            #iterate through list of URLs from above
    
    except IOError:
        print "Could not access web address "
        
    
if __name__ == '__main__':
  main()