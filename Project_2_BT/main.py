from BinaryTree import *


# Fun. LCA for nodes
# works for BinaryTree if first parameter is "tree.root"

# def closest_parent(tree: BinaryTree, first_node: BinaryNode, second_node: BinaryNode) -> BinaryNode:
#     if tree is None:
#         return None
#     if tree is first_node or tree is second_node:
#         return tree
#     left = closest_parent(tree.left_child, first_node, second_node)
#     right = closest_parent(tree.right_child, first_node, second_node)
#     if left is not None and right is not None:
#         return tree
#     if left is not None:
#         return left
#     return right


def closest_parent(tree: BinaryTree, first_node: BinaryNode, second_node: BinaryNode) -> BinaryNode:
    tree_temp = tree.root

    def closest_parent_node(tree_subfun, first_node_subfun, second_node_subfun):
        if tree_subfun is None:
            return None
        if tree_subfun is first_node_subfun or tree_subfun is second_node_subfun:
            return tree_subfun
        left = closest_parent_node(tree_subfun.left_child, first_node_subfun, second_node_subfun)
        right = closest_parent_node(tree_subfun.right_child, first_node_subfun, second_node_subfun)
        if left and right:
            return tree_subfun
        if left:
            return left
        return right
    return closest_parent_node(tree_temp, first_node, second_node)


# Tests:
tree = BinaryTree(1)
tree.root.add_left_child(2)
tree.root.add_right_child(3)
tree.root.right_child.add_right_child(7)
tree.root.left_child.add_left_child(4)
tree.root.left_child.add_right_child(5)
tree.root.left_child.left_child.add_left_child(8)
tree.root.left_child.left_child.add_right_child(9)

print("\nBinary tree from example:")
tree.show()

print("For nodes with values " + str(tree.root.left_child.left_child.left_child) +
      " and " + str(tree.root.left_child.right_child) + " the result will be node with value:\n" +
      str(closest_parent(tree, tree.root.left_child.left_child.left_child, tree.root.left_child.right_child)))


print("For nodes with values " + str(tree.root.left_child.left_child.right_child) +
      " and " + str(tree.root.right_child.right_child) + " the result will be node with value:\n" +
      str(closest_parent(tree, tree.root.left_child.left_child.right_child, tree.root.right_child.right_child)))




