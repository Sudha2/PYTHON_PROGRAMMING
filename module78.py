#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      ELCOT
#
# Created:     10-02-2018
# Copyright:   (c) ELCOT 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
a=int(input("enter the no"))

if a < 0:
   print("Enter a number")
else:
   sum = 0
   while(a > 0):
       sum += a
       a -= 1
   print("The sum is",sum)