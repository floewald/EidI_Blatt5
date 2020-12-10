# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
def add_up(tree):
    return add_up_aux(tree, 1)

def add_up_aux(tree, level):
    if type(tree) == tuple:
        treesum = level*tree[1] + add_up_aux(tree[0], level+1) + add_up_aux(tree[2], level+1)
        return treesum
    elif type(tree) == int:
        return level*tree

tree = ((111, -16, -26), 81, -7)
tree = ((3,5,-26),4,((3,3,2),1,((-12,9,120),-11,7)))
# tree = (-26, 81, -7)
print(add_up(tree))
a = 111 -16 -26 + 81 - 7
# a = 3*111 -2*16 -3*26 + 81 - 2*7
print(a)
# print("290")
print("547")