def char_dict(target_str):
	if not target_str:
		print "null string"
		return False

	hash_table = {}

	for char in target_str:
		if char not in hash_table.keys():
			hash_table[char] = 0
		else:
			hash_table[char] += 1

	return hash_table 

def check_permutation(str_1, str_2):
	if not str_1 or not str_2:
		print "null string"
		return False

	if char_dict(str_1) == char_dict(str_2):
		return True
	else:
		return False

if __name__ == '__main__':
	my_str_1 = "hello world!"
	my_str_2 = "world hello"

	print check_permutation(my_str_1, my_str_2)