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

def replace_space(target_str):
    if not target_str:
        print "target string is NULL"
        return False

    str_list = list(target_str)

##    for char in str_list:
##        if char == " ":
##            char = "%20"

    for pos in range(0, len(str_list)):
        if str_list[pos] == ' ':
            str_list[pos] = "%20"

    new_str = "".join(str_list)

    return new_str

if __name__ == '__main__':
    my_str = "hello world"
    print replace_space(my_str)
