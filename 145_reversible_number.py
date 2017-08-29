max_len = 3


def rec(digits):
    l = len(digits)
    if l == 0:
        return [l for i in range(1, 10) for l in rec([i])]
    elif l >= max_len:
        return [digits]
    elif l <= max_len / 2:
        return [l for i in range(10) for l in rec(digits + [i])]
    elif l == max_len / 2 + 1:
        if digits[-1] + digits[max_len-l] > 9:
            if digits[max_len-l-1] % 2 == 0:
                return [l for i in range(max(10-digits[-2], 1 if l == max_len-1 else 0), 10, 2) for l in rec(digits + [i])]
            else:
                return [l for i in range(max(10-digits[-2], 1), 10, 2) for l in rec(digits + [i])]
        else:
            if digits[max_len-l-1] % 2 == 0:
                return [l for i in range(max(10-digits[-2], 1), 10, 2) for l in rec(digits + [i])]
            else:
                return [l for i in range(max(10-digits[-2], 1 if l == max_len-1 else 0), 10, 2) for l in rec(digits + [i])]
    else:
        if digits[-1] + digits[max_len-l] > 9:
            if digits[max_len-l-1] % 2 == 0:
                return [l for i in range(1 if l == max_len-1 else 0, 10, 2) for l in rec(digits + [i])]
            else:
                return [l for i in range(1, 10, 2) for l in rec(digits + [i])]
        else:
            if digits[max_len-l-1] % 2 == 0:
                return [l for i in range(1, 10, 2) for l in rec(digits + [i])]
            else:
                return [l for i in range(1 if l == max_len-1 else 0, 10, 2) for l in rec(digits + [i])]

r = rec([])
print len(r), r
