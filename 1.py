

def decorator_1(func):
    def good(a, b):
        ret = func(a, b)
        return abs(ret)
    return good


@decorator_1
def add(add_a, add_b):
    if add_a > add_b:
        return add_a + add_b
    else:
        return add_a - add_b


print(add(1, 6))
print(add(1, 8))


