class LinkedNode:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = LinkedNode(0, 0)
        self.tail = LinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addNode(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
        node = LinkedNode(key, value)
        self.addNode(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            rmvNode = self.head.next
            self.removeNode(rmvNode)
            del self.cache[rmvNode.key]

    def removeNode(self, node):
        temp_prev = node.prev
        temp_next = node.next
        temp_prev.next = temp_next
        temp_next.prev = temp_prev

    def addNode(self, node):
        temp = self.tail.prev
        temp.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = temp


# Input Pattern
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
