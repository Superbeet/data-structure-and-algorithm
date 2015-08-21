
"""
0 1 2 3 4 5 6
1 a b c d e f
2 a b c d e f
3 a b c d e f
4 a b c d e f
5 a b c d e f
6 a b c d e f
"""
import copy

def print_matrix(target_matrix):
	x_axis = [ str(i) for i in range(0, len(target_matrix)+1) ]
	print ' '.join(x_axis)

	row_num = 0
	for row in target_matrix:
		row_num += 1
		row_items = ' '.join(row)
		print "%d %s" %(row_num, row_items)

def rotate_image(target_matrix):

    start_level = 0

    end_level = len(target_matrix)/2

    start_index = 0
##    end_index = end_level - start_index

    for level in range(start_level , end_level-start_level):

        start_index = level

        end_index = len(target_matrix) - start_index - 1

        print "[start_level, end_level, level][start_index, end_index] -> %s%s"\
            %([start_level, end_level, level],[start_index, end_index])

        top = copy.deepcopy(target_matrix[level][start_index:end_index])
        print "top ->", top

        for index in range(start_index, end_index-start_index):

            target_matrix[level][index] = target_matrix[end_index-index][level]
            target_matrix[index][level] = target_matrix[end_level-level][index]
            target_matrix[end_level][index] = target_matrix[end_index-index][end_level]
            target_matrix[index][end_level-level] = top[index]

        top = []

        print_matrix(target_matrix)

    return target_matrix

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

    print "----------------------"

    new_matrix = rotate_image(my_matrix)

    print "----------------------"

    print_matrix(new_matrix)