l = [1, 5, 5, 3, 1, 2, 2, 2, 1, 0, 4]
# d = {0: 1, 1: 3, 2: 3, 3: 1, 4: 1, 5: 2}
d = dict()

    # if x not in d:
    #     d[x] = 1
    # else:
    #     d[x] = d[x] + 1
for x in l:
    d[x] = d.get(x, 0) + 1
print(d)