#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      ELCOT
#
# Created:     17-04-2018
# Copyright:   (c) ELCOT 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


lower_limit = int(input("Enter the lower limit : "))
upper_limit = int(input("Enter the upper limit : "))
for i in range(lower_limit,upper_limit+1):
  if(i%4== 0):
    print(i)