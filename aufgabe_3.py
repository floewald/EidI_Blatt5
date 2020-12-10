# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
# def add_up(tree):
#     level   = 1
#     branch  = []
#     for m in range(0,3,2):
#         if type(tree[m]) == tuple:
#             tmp = add_up(tree[m])
#             branch.append(tmp)
#         else:
#             branch.append(tree[m])

#     print(branch)
#     return tree[1] +sum(branch)

def add_up(tree):
    def add_up_aux(tree, level):
        return level*tree
    level = 1
    branch = 0
    for m in range(0, 3, 2):
        if type(tree[m]) == tuple:
            level += 1
            branch += add_up_aux(tree[1], level) + add_up(tree[m])
        else:
            branch+= add_up_aux(tree[1], 1)
    print(branch)
    return branch



tree = ((111, -16, -26), 81, -7)
# tree = (-26, 81, -7)
print(add_up(tree))
a = 111 -16 -26 + 81 - 7
# a = 3*111 -2*16 -3*26 + 81 - 2*7
print(a)
print("290")