class ListNode:

    def __init__(self, val = -1):
        self.data = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next

        i = 0

        while curr:
            if i == index:
                return curr.data
            i += 1
            curr = curr.next
        
        return -1

    def insertHead(self, val: int) -> None:
        
        # New node
        temp = self.head.next
        n = ListNode(val)

        self.head.next = n
        n.next = temp

        if not n.next:
            self.tail = n


    def insertTail(self, val: int) -> None:

        self.tail.next = ListNode(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:

        i = 0

        curr = self.head

        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr

            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:

        res = []
        curr = self.head.next
        while curr:
            res.append(curr.data)
            curr = curr.next
        
        return res
        
