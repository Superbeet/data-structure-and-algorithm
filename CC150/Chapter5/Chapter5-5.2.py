# Chapter 5 - 5.2

import os
import sys

def printBinary(num):

	if num<0 or num>1:
	
		return False
	
	binary_list = []
	
	binary_list = ["0","."]
	
	while(num>0):
	
		if len(binary_list)>=32:
			return False
		
		r = num*2
		
		if r>=1:
			binary_list.append("1")
			num = r-1
		else:
			binary_list.append("0")
			num = r
		
	binary_str = "".join(binary_list)
	
	# print "binary_str->%s" %(binary_str)
	
	return binary_str

# def dec_to_hex(dic_num):
	
	# print "dic_num->", dic_num
	
	# hex_str = float.hex(dic_num)
	
	# return hex_str[2:-3]
	
# def hex_to_binary(hex_num):
	
	# print "hex_num->", hex_num
	
	# hex_size = len(hex_num) * 4
	
	# intergral = hex_num.split(".")[0]
	# fractional = hex_num.split(".")[1]
	
	# print "intergral->", intergral
	
	# h = hex_num[2:]
	
	# b_intergral = (bin(int(h, 16))[2:]).zfill(len(intergral))
	# b_fractional = (bin(int(h, 16))[2:]).zfill(len(fractional))
	
	# binary_num = "%s.%s" %(b_intergral, b_fractional)
	
	# return binary_num

# def dec_to_bin(dic_num):
	
	# temp = dec_to_hex(dic_num)
	
	# return hex_to_binary(temp)
	

if __name__ == '__main__':

	float_num = 0.625
	
	print printBinary(float_num)

	
	
	
	