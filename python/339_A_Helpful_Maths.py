def sol():
    str_in = input()
    splitted = str_in.split('+')
    splitted.sort()
    out = '+'.join(splitted)
    return out

print(sol())
