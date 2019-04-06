
# with open('weapon.txt', encoding='utf-8') as f:
#     print(f.read())


# i = 0
# with open('weapon.txt', encoding='utf-8') as f:
#     for line in f.readlines():
#         i += 1
#         print(line.strip())
# print("%d" % i)

with open('weapon.txt', encoding='utf-8') as f:
    for line in f:
        print(line.strip())