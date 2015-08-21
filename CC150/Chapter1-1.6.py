
"""
0 1 2 3 4 5 6
1 a b c d e f
2 a b c d e f
3 a b c d e f
4 a b c d e f
5 a b c d e f
6 a b c d e f
"""

def print_matrix(target_matrix):
	x_axis = [ str(i) for i in range(0, len(target_matrix)+1) ]
	print ' '.join(x_axis)

	row_num = 0
	for row in target_matrix:
		row_num += 1
		row_items = ' '.join(row)
		print "%d %s" %(row_num, row_items)

def rotate_image(target_str):
	if len(target_str):
		pass


if __name__ == '__main__':
	my_matrix = [
		['a','b','c','d','e','f'],
		['a','b','c','d','e','f'],
		['a','b','c','d','e','f'],
		['a','b','c','d','e','f'],
		['a','b','c','d','e','f'],
		['a','b','c','d','e','f'],
	]

	print_matrix(my_matrix)