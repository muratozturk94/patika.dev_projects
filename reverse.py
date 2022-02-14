def reverse(lst):
    if len(lst) == 0:
        return []
    if type(lst[-1]) == list:
        return [reverse(lst[-1])] + reverse(lst[:-1])
    else:
        return [lst[-1]] + reverse(lst[:-1])
