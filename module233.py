#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ELCOT
#
# Created:     10-04-2018
# Copyright:   (c) ELCOT 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
number=int(input("enter a number:"))
if number>1:
    for i in range(2,number):
        if(number%i)==0:
            print("no")
            break
    else:
     print("yes")
else:
    print("no")





