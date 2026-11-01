from collections import deque

class MyStack:

    def __init__(self):
        # q1 [a,b,c], q2 []
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        # q1 [a,b,c], q2 [x]
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())
        
        # q2 [x,a,b,c]
        self.q1, self.q2 = self.q2, self.q1

        # q1 [x,a,b,c], q2[]
        

    def pop(self) -> int:
        return self.q1.popleft()
        

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()