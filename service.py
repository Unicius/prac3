def check(values, capacity):
    if not isinstance(values, list):
        return "TYPE"
    if not values:
        return "EMPTY"
    if len(values) > capacity:
        return "OVERLOAD"
    for x in values:
        if type(x) not in (int, float) or not 0 <= x <= 60:
            return "BAD_ITEM"
    return "OK"
