def sol():
    mxn=[int(x) for x in input().strip().split()]
    m = mxn[0]
    n = mxn[1]
    area = m*n
    dominos = area//2
    return dominos
print(sol())
