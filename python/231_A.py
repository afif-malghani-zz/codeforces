def solutions():
    count = 0
    probs = int(input())
    binaries = []
    for i in range(probs):
        binaries.append([int(x) for x in input().strip().split()])
    for bin_ in binaries:
        if bin_.count(1) > 1:
            count += 1
    return count
print(solutions())
