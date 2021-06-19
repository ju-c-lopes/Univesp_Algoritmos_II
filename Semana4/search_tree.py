from BSTNode import BSTNode

tree = BSTNode(8)
tree.left = BSTNode(3)
tree.left.left = BSTNode(1)

tree.left.right = BSTNode(6)
tree.left.right.right = BSTNode(7)
tree.left.right.left = BSTNode(4)

tree.right = BSTNode(10)
tree.right.right = BSTNode(14)

# found = tree.get(4)
# if found:
#     print(found)
