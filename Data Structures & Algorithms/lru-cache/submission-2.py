class ListNode:
    def __init__(self):
        self.nxt = self.prev = None
        self.val = self.key = None


class LRUCache:

    def __init__(self, capacity: int):
        self.Hmap = {}
        self.left = ListNode()
        self.right = ListNode()
        self.left.nxt = self.right
        self.right.prev = self.left
        self.capacity = capacity

        # right = LRU
        # left = MRU
        

    def get(self, key: int) -> int:
        # if it exists
        # remove node from LL
        if key in self.Hmap:
            self.remove(self.Hmap[key])
            self.insert(self.Hmap[key])
            return self.Hmap[key].val
        # else return 1
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.Hmap:
            # if the key already exists, we just update its value
            self.Hmap[key].val = value
            self.remove(self.Hmap[key])
            self.insert(self.Hmap[key])
        elif len(self.Hmap) == self.capacity:
            to_remove = self.right.prev
            #remove lru from Hmap
            del self.Hmap[to_remove.key]
            # remove lru from LL
            self.remove(to_remove)

            # add new key to LL
            node = ListNode()
            node.key = key
            node.val = value
            self.Hmap[key] = node
            self.insert(node)
        else:
            node = ListNode()
            node.key = key
            node.val = value
            self.Hmap[key] = node
            self.insert(node)

    
    def insert(self, node: ListNode):
        prev = self.left
        nxt = self.left.nxt
        node.prev = prev
        node.nxt = nxt
        nxt.prev = prev.nxt = node


    
    def remove(self, node: ListNode):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev

        
