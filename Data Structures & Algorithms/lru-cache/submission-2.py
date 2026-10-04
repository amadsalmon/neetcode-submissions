class Node:
    def __init__(self, key: int, value: int, prev: Optional[Node], next: Optional[Node]):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    """
    Doubly Linked List (DLL)
    Back (least recently used) -> ... -> Front (most recently used)
    """
    def __init__(self):
        self.back = None
        self.front = None
    
    def moveToFront(self, node: Node) -> None:
        if self.isEmpty():
            self.back = node
            self.front = node
            return
        
        elif node == self.front:
            # Do nothing if the node is already at the front
            return
        
        node_was_back = (node == self.back)


        # Swap node to the front to make it the most recently used
        #   1 - Start by extracting it from its previous location, stitching its gap together
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if node_was_back:
            self.back = self.back.next
            self.back.prev = None
        
        #   2 - Now make it the front of the DLL
        node.prev = self.front
        self.front.next = node
        node.next = None
        self.front = node

        

    
    def putInList(self, node: Node) -> None:
        if self.isEmpty():
            self.back = node
            self.front = node
            return

        if self.hasOnlyOneElement():
            self.back.next = node
            self.front = node
            self.front.prev = self.back
            return

        node.prev = self.front
        self.front.next = node
        self.front = node


    def putInListAndPopOldest(self, node: Node) -> Node:
        node.prev = self.front
        self.front.next = node
        self.front = node

        # Pop oldest and replace it with second oldest:
        old_back = self.back
        self.back = self.back.next
        self.back.prev = None
        return old_back
    
    def isEmpty(self) -> bool:
        return self.back == self.front == None
    
    def hasOnlyOneElement(self) -> bool:
        return self.back == self.front and not self.isEmpty()

"""
Test dry run:
["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]


cache: {
1: 1
2: 2
}

DLL: 
1
1
1 -> 2
"""

            
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # Doubly linked list to keep track of recency of usage
        self.dll = DoublyLinkedList()


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.dll.moveToFront(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.dll.moveToFront(node)
            self.cache[key] = node
        else:
            new_node = Node(key, value, None, None)
            if len(self.cache) == self.capacity:
                popped_node = self.dll.putInListAndPopOldest(new_node)
                self.cache.pop(popped_node.key, None)
            else:
                self.dll.putInList(new_node)
            self.cache[key] = new_node



        