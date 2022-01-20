count = int(input())
strings = []
for i in range(count):
    string_in = input()
    strings.append(string_in)
for string_in in strings:
    if len(string_in) > 10:
        strings[strings.index(string_in)] = string_in[0] + str(len(string_in)-2)+string_in[-1]
for strin in strings:
    print(strin)
