from typing import Any, Callable, List
import treelib as tl
from binarytree import build
from Task1 import Queue


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        return str(self.value)

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

    def traverse_level_order(self, visit: Callable[[Any], None]) -> None:
        q = Queue()
        q.enqueue(self)
        while len(q) > 0:
            node = q.dequeue()
            if node is None:
                continue
            visit(node)
            q.enqueue(node.left_child)
            q.enqueue(node.right_child)

    # def min(self) -> 'BinaryNode':
    #     if self.left_child is not None:
    #         return self.left_child.min()
    #     return self

    def min(self) -> 'BinaryNode':
        nodes_values_list = []

        def add_values(node: BinaryNode) -> None:
            nodes_values_list.append(node.value)

        self.traverse_in_order(add_values)
        min_val = nodes_values_list[0]
        for x in nodes_values_list:
            if x < min_val:
                min_val = x
        return min_val

    def contains_(self, value: Any) -> bool:
        if value == self.value:
            return True
        if value < self.value:
            if self.left_child is not None:
                return self.left_child.contains_(value)
            else:
                return False
        if value > self.value:
            if self.right_child is not None:
                return self.right_child.contains_(value)
            else:
                return False


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, value: Any) -> None:
        self.root = BinaryNode(value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value < node.value:
            if node.left_child is None:
                node.left_child = BinaryNode(value)
            else:
                self._insert(node.left_child, value)
        else:
            if node.right_child is None:
                node.right_child = BinaryNode(value)
            else:
                self._insert(node.right_child, value)
        return node

    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)

    def insertlist(self, list_: List[Any]) -> None:
        for value in list_:
            self.insert(value)

    def contains(self, value: Any) -> bool:
        return self.root.contains_(value)

# Incorrect pattern (works only for leaves)
    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value == node.value:
            if (node.left_child is None) & (node.right_child is None):
                return None
            elif node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
        node.value = node.right_child.min().value
        node.right_child = self._remove(node.right_child, node.value)
        if value < node.value:
            node.left_child = self._remove(node.left_child, value)
        else:
            node.right_child = self._remove(node.right_child, value)
        return node

    def remove(self, value: Any) -> None:
        self.root = self._remove(self.root, value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def traverse_level_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_level_order(visit)

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


# Lib is not correct
# def show(self) -> None:
#     nodes_values_list = []
#
#     q = Queue()
#     q.enqueue(self.root)
#     while len(q) > 0:
#         node = q.dequeue()
#         if node is None:
#             nodes_values_list.append(None)
#         if node is None:
#             continue
#         nodes_values_list.append(node.value)
#         q.enqueue(node.left_child)
#         q.enqueue(node.right_child)
#
#     tree_show = build(nodes_values_list)
#     print(tree_show)


# Tree:
tree = BinarySearchTree(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insertlist([14, 4, 7, 13])
# tree.insert(4)
# tree.insert(7)
# tree.insert(13)

tree.show()

print(tree.contains(5))
print(tree.contains(4))

# print("Post order:")
# tree.traverse_post_order(print)
# print("\nPre order:")
# tree.traverse_pre_order(print)
# print("\nIn order:")
# tree.traverse_in_order(print)
# print("\nLevel order:")
# tree.traverse_level_order(print)
