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

def reverseStr(res_str):
    if not res_str:
        print "null string"
        return False

    char_list = list(res_str)

    for pos in range(0, len(char_list)/2):
        temp = char_list[pos]
        char_list[pos] = char_list[len(res_str)-pos-1]
        char_list[len(res_str)-pos-1] = temp

    new_str = "".join(char_list)

    return new_str

if __name__ == '__main__':
    res_str = "hello world"
    print reverse(res_str)
