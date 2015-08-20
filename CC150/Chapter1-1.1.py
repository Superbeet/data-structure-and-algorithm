def check_duplicate_char(res_str):
	if not res_str:
		print "null string"
		return False

	hash_table = {}

	for char in res_str:
		if char not in hash_table.keys():
			hash_table.update({char:1})
		else:
			hash_table[char] += 1
			print "duplicate char -> %s"%char

	return hash_table

if __name__ == '__main__':
	my_str = "abccccdefghijjjjjkkkkk"
	check_duplicate_char(my_str)