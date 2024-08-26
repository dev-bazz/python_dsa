# BigO used to calculate the performance of an application.
# We have time complexity and space complexity

def n_complexity(arg:list)-> None:
    """
    O(n)
    this means the larger te dataset the longer it takes

    """
    update_arg = [int(x) * 2 for x in arg]
    print('update_arg: ', update_arg)


n_complexity([1,2,3,4,5,6,7,8,9,10])