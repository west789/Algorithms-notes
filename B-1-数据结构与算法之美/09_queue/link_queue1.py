from typing import Optional


class Node:

    def __init__(self, data: str, next=None):
        self.data = data
        self._next = next


class LinkedQueue:

    def __init__(self):
        self._head = None
        self._tail = None

    # def enqueue(self, item: str):
    #     new_node = Node(item)
    #     if self._tail:
    #         self._tail._next = new_node
    #     else:
    #         self._head = new_node
    #     self._tail = new_node
    def enqueue(self, value: str):
        new_node = Node(value)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node

    def dequeue(self):
        if self._head:
            value = self._head.data
            self._head = self._head._next
            if not self._head:
                self._head = None
            return value

    def __repr__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current._next
        return "->".join(value for value in values)


if __name__ == "__main__":
    link_queue = LinkedQueue()
    for i in range(10):
        link_queue.enqueue(str(i))
    print(link_queue)

    for _ in range(3):
        link_queue.dequeue()
    print(link_queue)

    link_queue.enqueue("7")
    link_queue.enqueue("8")
    print(link_queue)
