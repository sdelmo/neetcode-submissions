class Node:

    def __init__(self, val):

        self.data = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head, self.tail = Node(-1), Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        # Append at end of queue

        new_node = Node(value)
        predecessor = self.tail.prev

        new_node.prev = predecessor
        new_node.next = self.tail
        predecessor.next = new_node
        
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:

        successor = self.head.next

        new_node = Node(value)
        
        new_node.next = successor
        new_node.prev = self.head

        successor.prev = new_node

        self.head.next = new_node
        

    def pop(self) -> int:

        if self.head.next == self.tail:
            return -1
        
        else:
            # otherwise dequeue an element from the end

            popped_element = self.tail.prev
            previous_element = self.tail.prev.prev
            # now deal with removing it
            previous_element.next = self.tail
            self.tail.prev = previous_element

            return popped_element.data

    def popleft(self) -> int:

        if self.head.next == self.tail:
            return -1
        
        else:
            popped_element = self.head.next
            successor = self.head.next.next

            self.head.next = successor
            successor.prev = self.head

            return popped_element.data
        
