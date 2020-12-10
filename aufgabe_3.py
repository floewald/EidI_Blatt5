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

def update_tree(tree):
    return update_tree_aux(tree, 1)

def update_tree_aux(tree, level):
    if (type(tree[0]) == int) and (type(tree[2]) == int):
        return (tree[0], level*(tree[0] + tree[2]), tree[2])
    elif (type(tree[0]) == tuple) and (type(tree[2]) == int):
        branch1 = update_tree_aux(tree[0], level+1)
        branch2 = tree[2]
        return (branch1, level*(branch1[1] + branch2), branch2)
    elif (type(tree[0]) == int) and (type(tree[2]) == tuple):
        branch1 = tree[0]
        branch2 = update_tree_aux(tree[2], level+1)
        return (branch1, level*(branch1 + branch2[1]), branch2)
    elif (type(tree[0]) == tuple) and (type(tree[2]) == tuple):
        branch1 = update_tree_aux(tree[0], level+1)
        branch2 = update_tree_aux(tree[2], level+1)
        return (branch1, level*(branch1[1]+branch2[1]), branch2)

## task 3 a
# tree = ((111, -16, -26), 81, -7)
# tree = ((3,5,-26),4,((3,3,2),1,((-12,9,120),-11,7)))
# # tree = (-26, 81, -7)
# print(add_up(tree))
# a = 111 -16 -26 + 81 - 7
# # a = 3*111 -2*16 -3*26 + 81 - 2*7
# print(a)
# # print("290")
# print("547")

## task 3b
# tree = ((111,-16,-26),81,-7)
tree = ((3,5,-26),4,((3,3,2),1,((-12,9,120),-11,7)))
print(update_tree(tree))
((3,-46,-26),2618,((3,15,2),2664,((-12,432,120),1317,7)))