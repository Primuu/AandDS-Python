from typing import Any, Callable
import treelib as tl


class BinaryNode:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        return str(self.value)

    def is_leaf(self) -> bool:
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)


class BinaryTree:
    root: BinaryNode

    def __init__(self, value: Any) -> None:
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self) -> None:
        tree_tl = tl.Tree()
        tree_tl.create_node(str(self.root.value), str(self.root.value))

        def create_node_tl(node: 'BinaryNode') -> None:
            if node.right_child is not None:
                tree_tl.create_node(str(node.right_child.value), str(node.right_child.value), parent=str(node.value))
            if node.left_child is not None:
                tree_tl.create_node(str(node.left_child.value), str(node.left_child.value), parent=str(node.value))

        self.traverse_pre_order(create_node_tl)
        tree_tl.show()


# Tests:
tree = BinaryTree(10)
tree.root.add_left_child(9)
tree.root.add_right_child(2)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_right_child(6)

tree.show()

assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
print("Post order:")
tree.traverse_post_order(print)
print("Pre order:")
tree.traverse_pre_order(print)
print("In order:")
tree.traverse_in_order(print)

# Works for BinaryNode
# bn1 = BinaryNode(10)
# bn1.add_left_child(9)
# bn1.add_right_child(2)
# bn1.left_child.add_left_child(1)
# bn1.left_child.add_right_child(3)
# bn1.right_child.add_left_child(4)
# bn1.right_child.add_right_child(6)
# print()
# bn1.traverse_in_order(print)
# print()
# bn1.traverse_post_order(print)
# print()
# bn1.traverse_pre_order(print)
# print()
