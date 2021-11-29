from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        length = 0
        el_iterator = self.head
        if el_iterator is None:
            return length
        length = 1
        while el_iterator.next:
            length += 1
            el_iterator = el_iterator.next
        return length

    def __str__(self) -> str:
        print_iterator = self.head
        print_value = ""
        while print_iterator is not None:
            print_value = print_value + str(print_iterator.value)
            print_iterator = print_iterator.next
            if print_iterator is not None:
                print_value = print_value + " -> "
        return print_value

    def push(self, new_value: Any) -> None:
        new_node = Node(new_value)
        if self.head is None:
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node

    def append(self, new_value: Any) -> None:
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def node(self, at: int) -> Node:
        returned_node = self.head
        if returned_node is None:
            return None
        i = 0
        while i != at:
            if returned_node.next is not None:
                returned_node = returned_node.next
                i += 1
            else:
                return None
        return returned_node

    def insert(self, new_value: Any, after: Node) -> None:
        new_node = Node(new_value)
        if after == self.tail:
            after.next = new_node
            self.tail = new_node
        new_node.next = after.next
        after.next = new_node

    def pop(self) -> Any:
        if self.head is None:
            return None
        if self.head.next is None:
            deleted_node_value = self.head.value
            self.head = self.head.next
            self.tail = None
            return deleted_node_value
        deleted_node_value = self.head.value
        self.head = self.head.next
        return deleted_node_value

    def remove_last(self) -> Any:
        last_empty = self.head
        while last_empty.next.next:
            last_empty = last_empty.next
        deleted_node_value = last_empty.next.value
        self.tail = last_empty
        last_empty.next = None
        return deleted_node_value

    def remove(self, after: Node) -> Any:
        if after is None:
            return None
        if after.next is None:
            return None
        if after.next == self.tail:
            self.tail = after
            after.next = None
            return None
        after.next = after.next.next


class Stack:
    def __init__(self) -> None:
        self._storage = LinkedList()

    def __len__(self) -> int:
        return len(self._storage)

    def __str__(self) -> str:
        print_value = ""
        for x in range(0, len(self._storage)):
            print_value += str(self._storage.node(x).value) + "\n"
        return print_value

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> Any:
        return self._storage.pop()


class Queue:
    def __init__(self) -> None:
        self._storage = LinkedList()

    def __len__(self) -> int:
        return len(self._storage)

    def __str__(self) -> str:
        print_value = ""
        for x in range(0, len(self._storage)):
            print_value += str(self._storage.node(x).value)
            if x + 1 < len(self._storage):
                print_value += ", "
        return print_value

    def peek(self) -> Any:
        return self._storage.head.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()


