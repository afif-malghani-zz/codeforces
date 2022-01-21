def sol():
    mat = []
    for i in range(5):
        row = [int(x) for x in input().strip().split()]
        mat.append(row)
    col_no = 0
    row_no = 0
    for i in mat:
        if 1 in i:
            row_no = mat.index(i)
            break
    for i in mat[row_no]:
        if i == 1:
            col_no= mat[row_no].index(i)
            break
    steps = abs(2-col_no) + abs(2-row_no)
    return steps
print(sol())
