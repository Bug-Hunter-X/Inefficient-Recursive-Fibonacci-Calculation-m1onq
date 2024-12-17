def function(x, memo={}):
    if x in memo:
        return memo[x]
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        result = function(x-1, memo) + function(x-2, memo)
        memo[x] = result
        return result