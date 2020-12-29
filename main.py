def is_valid_walk(walk):
    n = 0
    s = 0
    e = 0
    w = 0
    my_dict = {}
    if len(walk) > 10 or len(walk) < 10:
        return False
    else:
        print(walk)
        for direction in walk:
            print(direction)
            print(n, s, e, w)
            if direction == 'n':
                n += 1
                s -= 1
            elif direction == 's':
                s += 1
                n -= 1
            elif direction == 'e':
                e += 1
                w -= 1
            elif direction == 'w':
                w += 1
                e -= 1
        if n != s:
            return False
        elif e != w:
            return False
        else:
            return True