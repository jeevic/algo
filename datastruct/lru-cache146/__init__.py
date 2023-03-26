class LRUCache:
    """

    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.dbl = DobuleList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.make_recent(key)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.deleteKey(key)
            self.add_recent(key, value)
            return

        if self.dbl.get_size() == self.capacity:
            self.remove_least_recent()
        self.add_recent(key, value)
        return

    def remove_least_recent(self):
        node = self.dbl.remove_first()
        if node is None:
            return
        del self.map[node.key]

    def make_recent(self, key):
        node = self.map[key]
        self.dbl.remove_node(node)
        self.dbl.add_last(node)
        return

    def deleteKey(self, key):
        node = self.map.get(key)
        self.dbl.remove_node(node)
        del self.map[key]

    def add_recent(self, key, val):
        node = Node(key, val)
        self.dbl.add_last(node)
        self.map[key] = node


class DobuleList:

    def __init__(self):
        self.root = Node(None, None)
        self.tail = Node(None, None)
        self.size = 0

        self.root.next = self.tail
        self.tail.prev = self.root

    def remove_node(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1
        return

    def add_last(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
        return

    def remove_first(self):
        if self.root.next == self.tail:
            return None

        first = self.root.next
        self.root.next = first.next
        first.next.prev = self.root
        self.size -= 1
        return first

    def get_size(self):
        return self.size


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
