# naive example:
# this makes a copy of the list at EVERY RECURSIVE CALL!!!
def sum_list(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

#pythonic example:
def sum_list(lst):
    print('lst= ', lst)
    print('len(lst)= ', len(lst))
    # create a 'higher order' function inside the main function
    def helper(start_index):
        if start_index == len(lst):
            return 0
        print('adding ', lst[start_index])
        return lst[start_index] + helper(start_index + 1)
    return helper(0)

a_list = [2, 14, 5, 36, 7, 8, 94]