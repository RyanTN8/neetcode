class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.capacity = capacity
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.left.next = self.right
        self.right.prev = self.left


    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        
        node = self.hashMap[key]
        self.remove(node)
        self.insert(node)
        return node.val
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
        
        node = Node(key, value)
        self.insert(node)
        self.hashMap[key] = node

        if len(self.hashMap) > self.capacity:
            k = self.left.next.key
            self.remove(self.left.next)
            self.hashMap.pop(k, "None")
    
    #helper functions
    def remove(self, n: Node) -> None:
        prevNode = n.prev
        nextNode = n.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insert(self, n: Node) -> None:
        prev = self.right.prev
        prev.next = n
        n.prev = prev
        n.next = self.right
        self.right.prev = n
            
