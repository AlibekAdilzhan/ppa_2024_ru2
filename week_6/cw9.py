list1 = ["a", "b", "c", 1, 1, 1]

for i in range(len(list1)):
    print(list1[i], end=" ")
print()
for x in list1:
    print(x, end=" ")
print()
print(*list1)