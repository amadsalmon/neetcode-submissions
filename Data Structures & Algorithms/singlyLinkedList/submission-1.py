class Node:
    def __init__(self, val: int, next: Optional[Node] = None):
        self.val = val
        self.next = next
    
class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while current and i < index:
            current = current.next
            i += 1
        return current.val if current else -1 
        

    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new
        

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(val)


    def remove(self, index: int) -> bool:
        if not self.head:
            return False
            
        if index == 0:
            self.head = self.head.next
            return True   
        
        current = self.head
        last = None
        i = 0
        while current and i < index:
            last = current
            current = current.next
            i += 1
        
        if current and last:
            last.next = current.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        res = []
        current = self.head
        while current:
            res.append(current.val)
            current = current.next
        return res
        

