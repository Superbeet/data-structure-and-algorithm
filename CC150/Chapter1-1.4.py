#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      507061
#
# Created:     20/08/2015
# Copyright:   (c) 507061 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import string

def string_compress(target_str):
    if not target_str:
        print "string is null"
        return False

    hash_table = {}

    diff = 0
    count = 0
    last_char = None
    new_str = ""

    for char in target_str:

        print "char-> %s" %char

        count += 1

        if last_char is not char:

            if last_char is not None:

                diff = diff + count - 2

                print count

                new_str += "%s%s" %(last_char, count)

            count = 0

        last_char = char

    new_str += "%s%s" %(last_char, count)

##    last_char = target_str[0]
##    new_str = ""
##
##    for char in target_str:
##
##        if char not in hash_table.keys():
##
##            hash_table.update({char:1})
##
##        hash_table[char] += 1
##
##        diff += (hash_table[char]-2)
##
##        if last_char != char:
##            new_str +="%s%s" %(last_char, hash_table[char])
##            hash_table[char] = 0
##
##        last_char = char
##    print diff

    if diff >= 0:
        return new_str

    else:
        return target_str

if __name__ == '__main__':
##    my_str = "aaaabbcdddeeefaaa"
    my_str = 'aabbccddeefff'
    print my_str
    print string_compress(my_str)
