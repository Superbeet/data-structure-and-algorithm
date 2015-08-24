from copy import deepcopy

def isSubstring(full_str, sub_str):

	full_str_length = len(full_str)
	sub_str_length = len(sub_str)

	# i = 0

	# while i < full_str_length:
	for i in range(0, full_str_length):
		m = i
		n = 0

		while m < full_str_length and n < sub_str_length \
			and full_str[m] == sub_str[n]:

			m += 1
			n += 1

		if n == sub_str_length:
			return True

	return False


def is_rotation(str_1, str_2):

	if len(str_1) == len(str_2) and len(str_1) > 0 and len(str_2) > 0:

		str_1_double = str_1 + str_1

		return isSubstring(str_1_double, str_2)

	else:

		return False



# print isSubstring('aaaabcdddd','abc')
print is_rotation('abcde','cdeab')


