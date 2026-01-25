def swap_case(s):
    res = []
    for c in s:
        if not (c >= 'A' and c <= 'Z') and not (c >= 'a' and c <= 'z'):
            res.append(c)
        elif c < 'a':
            res.append(chr(ord(c) - ord('A') + ord('a')))
        else:
            res.append(chr(ord(c) - ord('a') + ord('A')))
    return ''.join(res)
