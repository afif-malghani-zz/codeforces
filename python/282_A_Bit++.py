def sol():
    num = int(input())
    x = 0
    for i in range(num):
        inst = input()
        if '++' in inst:
            x += 1
        elif '--' in inst:
            x -= 1

    return x

print(sol())
