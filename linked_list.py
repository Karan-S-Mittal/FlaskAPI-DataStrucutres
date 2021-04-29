class Node:
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    def __str__(self) -> str:
        return self.data


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None

    def to_array(self):
        arr = []
        if self.head == None:
            return arr
        else:
            node = self.head
            while node:
                arr.append(node.data)
                node = node.next_node
            return arr

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node == None:
            print(None)
        while node.next_node != None:
            ll_string += f"{node.data} -> "
            node = node.next_node
        ll_string += "None"
        print(ll_string)

    def insert_beginning(self, data):
        if self.head == None:
            self.head = Node(data, None)
            self.last_node = self.head
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    def insert_at_end(self, data):
        if self.head == None:
            self.insert_beginning(data)
        else:
            self.last_node.next_node = Node(data, None)
            self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] == int(user_id):
                return node.data
            node = node.next_node
        return None
