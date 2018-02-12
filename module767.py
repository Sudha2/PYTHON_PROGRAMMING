#-------------------------------------------------------------------------------
# Name:        module7
# Purpose:
#
# Author:      ELCOT
#
# Created:     12-02-2018
# Copyright:   (c) ELCOT 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
mynam=6
n1=1
n2=2
count=0
if mynam<=0:
    print("plse enter a positive no")
elif mynam==1:
    print("Fibbanoci series upto",mynam)
    print(n1)
else:
    print("Fibbanoci series upto",mynam)
while count < mynam:
       print(n1,end=' ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
