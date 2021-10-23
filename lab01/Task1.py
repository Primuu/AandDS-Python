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

# First version (by iterating)
    # def append(self, new_value: Any) -> None:
    #     new_node = Node(new_value)
    #     if self.head is None:
    #         self.head = new_node
    #         return
    #     last_empty = self.head
    #     while last_empty.next:
    #         last_empty = last_empty.next
    #     last_empty.next = new_node

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


# -----------------------------------------------------------------------
# First assert
list1 = LinkedList()
assert list1.head is None
assert list1.tail is None


# Second assert
list1.push(1)
assert list1.tail is not None
# print(list1.tail.value)
list1.push(0)
assert str(list1) == '0 -> 1'
print("\nSecond assert (push): \n" + str(list1))
# print(list1.tail.value)


# Third assert
list1.append(9)
list1.append(10)
assert str(list1) == '0 -> 1 -> 9 -> 10'
print("\nThird assert (append): \n" + str(list1))
# print(list1.tail.value)


# Fourth  assert
middle_node = list1.node(at=1)
# print(str(middle_node.value) + " -> " + str(middle_node.next.value))
list1.insert(5, after=middle_node)
assert str(list1) == '0 -> 1 -> 5 -> 9 -> 10'
print("\nFourth assert (insert): \n" + str(list1))


# Fifth  assert
first_element = list1.node(at=0)
# print(first_element.value)
returned_first_element = list1.pop()
assert first_element.value == returned_first_element
print("\nFifth assert (pop): \n" + str(list1))


# Sixth  assert
last_element = list1.node(at=3)
returned_last_element = list1.remove_last()
assert last_element.value == returned_last_element
assert str(list1) == '1 -> 5 -> 9'
print("\nSixth assert (remove_last): \n" + str(list1))


# Seventh assert
second_node = list1.node(at=1)
list1.remove(second_node)
assert str(list1) == '1 -> 5'
print("\nSeventh assert (remove): \n" + str(list1))


# len fun.
list2 = LinkedList()
print("\n" + str(list2) + "\n Length(0): " + str(len(list2)))
list2.append(1)
print("\n" + str(list2) + "\n Length(1): " + str(len(list2)))
list2.append(2)
list2.append(3)
list2.append(4)
print("\n" + str(list2) + "\n Length(4): " + str(len(list2)) + "\n")


# -----------------------------------------------------------------------
# Stack asserts (1st)
stack = Stack()
assert len(stack) == 0

# Stack asserts (2nd)
stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3
print("\n\nStack asserts:\n" + str(stack))

# Stack asserts (3rd)
top_value = stack.pop()
assert top_value == 1
assert len(stack) == 2
print(stack)


# -----------------------------------------------------------------------
# Queue asserts (1st)
queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'
print("\n\nQueue asserts:\n" + str(queue))
# print(queue.peek())

# Queue asserts (2nd)
client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
print(queue)
