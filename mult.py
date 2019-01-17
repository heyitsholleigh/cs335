#!/usr/bin/env python3
import sys

def multiply(x, y):
  print(str(x * y))
  
if __name__ == '__main__':
  num1 = int(sys.argv[1])
  num2 = int(sys.argv[2])
  multiply(num1, num2)