# def factorial_recursive(n):
#     return n * factorial_recursive(n-1)
# ^^ THIS IS NOT FINISHED! ^^
# It has NO BASE CASE, so it will run forever


def factorial_recursive(n):
    # think: what is the smallest case?
    # when you get to 1, stop -
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

def factorial_recursive_edges(n):
    # what about edge cases? like what if input is 0 or less?
    if n <= 1:
        return 1
    return n * factorial_recursive_edges(n-1)