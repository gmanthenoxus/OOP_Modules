def histogram(lst):
    result = {}
    for item in lst:
        result[item] = result.get(item, 0) + 1
    return result

p