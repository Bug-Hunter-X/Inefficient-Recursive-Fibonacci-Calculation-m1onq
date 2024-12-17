def function(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return function(x-1) + function(x-2)