def backspace_compare(str1, str2):
    s1 = []
    s2 = []

    for c in str1:
        if c == '#':
            if s1:
                s1.pop()
        else:
            s1.append(c)

    for c in str2:
        if c == '#':
            if s2:
                s2.pop()
        else:
            s2.append(c)

    return s1 == s2
