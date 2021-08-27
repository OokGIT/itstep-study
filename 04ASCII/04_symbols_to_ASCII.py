def line(_str, size):
    a = _str * size
    return a


def hor_line(_str, size, space=False):
    a = ""
    for _ in range(size):
        if not space:
            a += "&\n"
        else:
            aa = "&"
            for i in range(8):
                aa += "-"

            a += aa + "&\n"
    return a


a = line('&', 10)
ba = hor_line('a', 4, space=True)
print(a)
print(ba.rstrip())
print(a)
