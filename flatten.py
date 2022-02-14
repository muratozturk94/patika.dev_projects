def flatten(lst):
    if lst == []:
        return []
    if type(lst[0]) == list:
        return flatten(lst[0] + flatten(lst[1:]))
    else:
        return [lst[0]] + flatten(lst[1:])
