#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ELCOT
#
# Created:     09-02-2018
# Copyright:   (c) ELCOT 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
list = ['guvi']
str=('guvi 5')
print(str)
def fun(x):
     print (x * 5)

def my_map_simple(fall, list):
     for item in list:
         fall(item)

my_map_simple(fun, list)
