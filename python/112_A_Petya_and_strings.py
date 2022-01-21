def sol():
    str1 = input().lower()
    str2 = input().lower()
    if str1 < str2:
        return -1
    elif str2 <str1:
        return 1
    elif str1 == str2:
        return 0

print(sol())