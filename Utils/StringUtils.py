def is_number(s):
    """returns True if string s can be cast to a number, False otherwise"""
    try:
        float(s)
        return True
    except ValueError:
        return False

# From this SO answer: http://stackoverflow.com/a/6043797/331047
def split_utf8(s, n):
    """Split UTF-8 s into chunks of maximum byte length n"""
    while len(s) > n:
        k = n
        while (ord(s[k]) & 0xc0) == 0x80:
            k -= 1
        yield s[:k]
        s = s[k:]
    yield s

# Taken from txircd
# https://github.com/ElementalAlchemist/txircd/blob/889b19cdfedd8f1bb2aa6f23e9a745bdf7330b81/txircd/modules/stripcolor.py#L4
def strip_colours(msg):
    """Strip colours (and other formatting) from the given string"""
    while chr(3) in msg:
        color_pos = msg.index(chr(3))
        strip_length = 1
        color_f = 0
        color_b = 0
        comma = False
        for i in range(color_pos + 1, len(msg) if len(msg) < color_pos + 6 else color_pos + 6):
            if msg[i] == ",":
                if comma or color_f == 0:
                    break
                else:
                    comma = True
            elif msg[i].isdigit():
                if color_b == 2 or (not comma and color_f == 2):
                    break
                elif comma:
                    color_b += 1
                else:
                    color_f += 1
            else:
                break
            strip_length += 1
        msg = msg[:color_pos] + msg[color_pos + strip_length:]
    # bold, italic, underline, plain, reverse
    msg = msg.replace(chr(2), "").replace(chr(29), "").replace(chr(31), "").replace(chr(15), "").replace(chr(22), "")
    return msg