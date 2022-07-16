def wash_dishes_iteratively(meals):
    for meal in meals:
        print('washing dishes from ', meal)

def wash_dishes_recursively(meals):
    # start with base case:
    # (it's standard practice to define base case FIRST)
    if len(meals) == 1:
        # meaning this is when there is only ONE meal,
        # so start it at meals list index 0 (the first meal)
        print('washing dishes from ', meals[0])
    #then deal with recursive case
    else:
        mid = len(meals)//2
        first_half = meals[:mid]
        second_half = meals[mid:]

        # first helper
        wash_dishes_recursively(first_half)
        # second helper
        wash_dishes_recursively(second_half)

        
meals = ['breakfast', 'lunch', 'snacks', 'dinner', 'bedtime tea']