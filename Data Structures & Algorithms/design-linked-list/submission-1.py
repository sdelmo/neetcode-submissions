class ListNode:
    def __init__(self, val=-1):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        # Set up "pseudo" head/tail
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        # Handle invalid index
        if index < 0 or index >= self.size:
            return -1

        if index < self.size - index:
            # search from the head
            c = self.head
            for _ in range(index + 1):
                c = c.next
        else:
            #search from the tail
            c = self.tail
            for _ in range(self.size - index):
                c = c.prev
        
        return c.val

    def addAtHead(self, val: int) -> None:
        succ, pred = self.head.next, self.head

        new_node = ListNode(val)
        # set pointer between head and new
        pred.next = new_node
        new_node.prev = pred

        # set pointer between new node and successor
        new_node.next = succ
        succ.prev = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        pred, succ = self.tail.prev, self.tail

        new_node = ListNode(val)

        pred.next = new_node

        new_node.prev = pred

        new_node.next = succ
        succ.prev = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        if index == self.size:
            self.addAtTail(val)
            return

        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            
            pred = succ.prev
        
        new_node = ListNode(val)
        pred.next = new_node
        new_node.prev = pred

        new_node.next = succ
        succ.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index >= self.size:
            return
        
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        
        pred.next = succ
        succ.prev = pred

        self.size -= 1
