from typing import Any, List, Callable, Union
from Task1 import Queue
import treelib as tl


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any) -> None:
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if not self.children:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def __str__(self) -> str:
        return str(self.value)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for child in self.children:
            child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        fifo = Queue()
        for child in self.children:
            fifo.enqueue(child)
        while len(fifo) > 0:
            visit(fifo.peek())
            for child in fifo.peek().children:
                fifo.enqueue(child)
            fifo.dequeue()

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        fifo = Queue()
        for child in self.children:
            fifo.enqueue(child)
        while len(fifo) > 0:
            if fifo.peek().value == value:
                return fifo.peek()
            for child in fifo.peek().children:
                fifo.enqueue(child)
            fifo.dequeue()
        return None


class Tree:
    root: TreeNode

    def __init__(self, value: Any) -> None:
        self.root = TreeNode(value)

    def add(self, value: Any, parent_name: Any) -> None:
        child = TreeNode(value)
        self.root.search(parent_name).add(child)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self) -> None:
        tree_tl = tl.Tree()
        tree_tl.create_node(str(self.root.value), str(self.root.value))

        def create_node_tl(node: 'TreeNode') -> None:
            for child in node.children:
                tree_tl.create_node(str(child.value), str(child.value), parent=str(node.value))

        self.for_each_level_order(create_node_tl)
        tree_tl.show()


tree = Tree("F")
tree.add("B", "F")
tree.add("G", "F")
tree.add("A", "B")
tree.add("D", "B")
tree.add("C", "D")
tree.add("E", "D")
tree.add("I", "G")
tree.add("H", "I")

tree.for_each_level_order(print)
print()
tree.for_each_deep_first(print)
print()
tree.show()


# Works for TreeNode
# treeNode1 = TreeNode('F')
# treeNode2 = TreeNode('B')
# treeNode3 = TreeNode('G')
# treeNode4 = TreeNode('A')
# treeNode5 = TreeNode('D')
# treeNode6 = TreeNode('I')
# treeNode7 = TreeNode('C')
# treeNode8 = TreeNode('E')
# treeNode9 = TreeNode('H')
#
# treeNode1.add(treeNode2)
# treeNode1.add(treeNode3)
# treeNode2.add(treeNode4)
# treeNode2.add(treeNode5)
# treeNode5.add(treeNode7)
# treeNode5.add(treeNode8)
# treeNode3.add(treeNode6)
# treeNode6.add(treeNode9)
# print(treeNode1.is_leaf())
# print(treeNode2.is_leaf())
# print(treeNode9.is_leaf())
#
# treeNode1.for_each_deep_first(print)
# print()
# treeNode1.for_each_level_order(print)
# print()
# print(treeNode1.search("H"))
# print(treeNode1.search("X"))
