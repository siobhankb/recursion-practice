# passing 'state'
from re import L


def sum_to_num(end_num, this_num, the_sum):
    #base case: return final state
    if this_num == end_num + 1:
        return the_sum
    else:
        # recursive case: thread state through recursive call
        return sum_to_num(end_num, this_num + 1, the_sum + this_num)


# pass in an initial state:
sum_to_num(10, 1, 0)


# Pass state GLOBALLY:
# (NOT RECOMMENDED - prevents using same variable names elsewhere; 
# uses up unnecessary memory)

# start by creating global variables
this_num = 1
the_sum = 0
end_num = 10

# define a function that takes no arguments
def global_sum():
    # call 'global' on variables to allow modification within the function
    global this_num
    global the_sum
    global end_num
    # base case:
    if this_num == end_num + 1:
        return the_sum
    # recursive case
    else:
        # need to update variables, since the function takes no arguments
        the_sum += this_num
        this_num += 1
    # call recursive function now that variables are taken care of
    return global_sum()

