#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ELCOT
#
# Created:     06-02-2018
# Copyright:   (c) ELCOT 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
l=input("enter the alphabet:")
if l in('a','e','i','o','u'):
    print("vowels")
elif l=='t':
    print("letter is either vowels or consonent")
else:
    print("consonant")
