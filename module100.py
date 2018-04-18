#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ELCOT
#
# Created:     18-04-2018
# Copyright:   (c) ELCOT 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num=371
sum = 0
temp=num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print("yes")
else:
   print("no")
