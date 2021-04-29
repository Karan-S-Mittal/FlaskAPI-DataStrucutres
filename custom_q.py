class Node:
    def __init__(self, data, next_node) -> None:
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.head is None and self.tail is None:
            self.tail = self.head = Node(data, None)
        else:
            self.tail.next_node = Node(data, None)
            self.tail = self.tail.next_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            removed = self.head
            self.head = removed.next_node

            if self.head is None:
                self.tail = None

            return removed
