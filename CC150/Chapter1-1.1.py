#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      507061
#
# Created:     19/08/2015
# Copyright:   (c) 507061 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def checkDuplicateChar(res_str):
    pos = 0
    hash_table = {}

    for char in res_str:
        # create a key-value pair if not existing
        if char not in hash_table.keys():
            hash_table.update({char:1})

        # inform if duplicate char is found
        if hash_table[char] > 0:
            hash_table[char] += 1

            print "Find duplicate char: %s"%(char)

if __name__ == '__main__':
    my_str = "abcddddefgggghiiii"
    checkDuplicateChar(my_str)

