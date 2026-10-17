class Node:
    def __init__(self, key=None, val=None, prev=None, next_=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next_ = next_

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}
        self.size = 0

    def get_element(self, key: int):
        if key not in self.cache:
            return -1
        
        val_node = self.cache[key]


        # prev = None / head
        if self.tail != val_node:      
            prev = val_node.prev
            next_ = val_node.next_
            if prev is not None:
                prev.next_ = next_
            else:
                self.head = next_
            if next_ is not None:
                next_.prev = prev
            self.tail.next_ = val_node
            val_node.prev = self.tail
            val_node.next = None

            self.tail = val_node

        # self.tail = self.tail.next_
        self.cache[key] = val_node

        return val_node
    
    def get(self, key: int) -> int:
        element = self.get_element(key)

        if element != -1:
            return element.val
        return -1

    def put(self, key: int, val: int) -> None:
        # print(val)
        if key in self.cache:
            element = self.get_element(key)
            if element != -1:
                element.val = val
        else:
            newNode = Node(key, val, None, None)
            if self.tail is not None:
                self.tail.next_ = newNode
                newNode.prev = self.tail
                self.tail = newNode
                print('--val', val)
            else:
                self.tail = newNode
                self.head = newNode
            
            self.cache[key] = newNode
            self.size += 1

            if self.size > self.capacity:
                first_key = self.head.key
                del self.cache[first_key]
                self.head = self.head.next_
                self.head.prev = None
                self.size -= 1
            





