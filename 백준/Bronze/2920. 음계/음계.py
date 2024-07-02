def check_scale(scale):
    ascending = list(range(1, 9))
    descending = list(range(8, 0, -1))
    
    if scale == ascending:
        return "ascending"
    elif scale == descending:
        return "descending"
    else:
        return "mixed"

scale = list(map(int, input().split()))

print(check_scale(scale))