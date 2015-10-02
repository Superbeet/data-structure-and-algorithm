# Write a function to determine the number of bits required to convert integer 1 to integer B.
'''
 10101010
&10101001
=10101000
&10100111
=10100000 
&10000001
=10000000
&01111111
=00000000
'''

import sys
import os

def NumOfConvert1(x, y):
	
	z = x^y
	
	count = 0
	
	while z:
		
		lsb = z&1
		
		if lsb == 1:
		
			count += 1
		
		z = z>>1
	
	return count

def NumOfConvert2(x, y):
	
	result = x^y
	
	count = 0
	
	while result:
		
		result = result & (result-1)
		
		count += 1
	
	return count	
	
if __name__ == '__main__':
	
	num1 = 1025
	
	num2 = 66
	
	print "num1 -> %32s" %(bin(num1))
	print "num2 -> %32s" %(bin(num2))
	
	print NumOfConvert1(num1, num2)
	print NumOfConvert2(num1, num2)