
"""
# 0 1 2 3 4 5
0 a b c d e f
1 a b c d e f
2 a b c d e f
3 a b c d e f
4 a b c d e f
5 a b c d e f
"""
from copy import deepcopy

def print_matrix(target_matrix):
    x_axis = [ str(i) for i in range(0, len(target_matrix)) ]
    x_axis.insert(0, "x")
    row_items = ' '.join(x_axis)
    print row_items

    row_num = 0
    for row in target_matrix:
        row_items = ' '.join(row)
        print "%d %s" %(row_num, row_items)
        row_num += 1

def rotate_image(target_matrix):

    size = len(target_matrix)

    start_level = 0

    end_level = size/2

    start_index = 0
    
    # print 'level->', range(start_level , end_level)

    for level in range(start_level , end_level):

        start_index = level

        end_index = size - level - 1

        # print 'index->', range(start_index, end_index)

        for index in range(start_index, end_index):

            offset = index - start_index

            # print 'offset->', offset

            top = target_matrix[level][index]

            target_matrix[level][index] = target_matrix[end_index-offset][level]
            target_matrix[end_index-offset][level] = target_matrix[size-level-1][end_index-offset]
            target_matrix[size-level-1][end_index-offset] = target_matrix[index][size-level-1]
            target_matrix[index][size-level-1] = top

    return target_matrix

if __name__ == '__main__':
    # my_matrix = [
    #         		['a','b','c','d','e','f'],
    #         		['a','b','c','d','e','f'],
    #         		['a','b','c','d','e','f'],
    #         		['a','b','c','d','e','f'],
    #         		['a','b','c','d','e','f'],
    #         		['a','b','c','d','e','f'],
    #         	]

    my_matrix = [
                    ['a','b','c','d','e'],
                    ['a','b','c','d','e'],
                    ['a','b','c','d','e'],
                    ['a','b','c','d','e'],
                    ['a','b','c','d','e'],
                ]

    print_matrix(my_matrix)

    print "----------------------"

    new_matrix = rotate_image(my_matrix)

    print_matrix(new_matrix)