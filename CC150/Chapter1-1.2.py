def reverse_string(res_str):
	if not res_str:
		return False

	str_list = list(res_str)

	for pos in range(0, len(str_list)/2):
		temp = str_list[pos]
		str_list[pos] = str_list[len(str_list)-1-pos]
		str_list[len(str_list)-1-pos] = temp

	new_str = "".join(str_list)

	return new_str

if __name__ == '__main__':
	my_str = "abcdefgh hello world"
	print reverse_string(my_str)
