from server import BlogPost


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def _insert_recursive(self, value, node):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(value, node.right)
        else:
            return

    def _search_recursive(self, blog_post_id, node):
        if node.left == None and node.right == None:
            return False

        if blog_post_id == node.data["id"]:
            return node.data

        if blog_post_id < node.data["id"]:
            if blog_post_id == node.left.data["id"]:
                return node.left.data
            else:
                return self._search_recursive(blog_post_id, node.left)

        if blog_post_id > node.data["id"]:
            if blog_post_id == node.right.data["id"]:
                return node.right.data
            else:
                return self._search_recursive(blog_post_id, node.right)

        return False

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def search(self, blog_post_id):
        if self.root is None:
            return False
        else:
            self._search_recursive(int(blog_post_id), self.root)
