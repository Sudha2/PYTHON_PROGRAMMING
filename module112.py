#-------------------------------------------------------------------------------
# Name:        module1
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
a=input()
b=input()
c=input()
if(a>=b)and(a>=c):
    print(a)
elif(b>=c)and(b>=c):
    print(b)
else:
    print("the largest no is",a and b and c)