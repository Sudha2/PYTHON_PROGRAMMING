#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      ELCOT
#
# Created:     10-04-2018
# Copyright:   (c) ELCOT 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


lower=1
upper=6
for num in range(lower +2,upper ):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)