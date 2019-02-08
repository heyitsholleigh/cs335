#!/usr/bin/python
import os

def main():

   for i in [11,9,0,2,1]:
       try:
           print "The answer is: %d" % (100/i)
       except Exception:
           print "Cant divide by 0"
           print Exception

               