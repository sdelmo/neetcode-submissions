class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next, self.prev = None, None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        self.curr_page = self.home

    def visit(self, url: str) -> None:
        new_pg = ListNode(url)

        new_pg.prev = self.curr_page
        self.curr_page.next = new_pg

        self.curr_page = self.curr_page.next
        

    def back(self, steps: int) -> str:
        while self.curr_page.prev and steps > 0:
            self.curr_page = self.curr_page.prev
            steps -= 1
        return self.curr_page.val
        

    def forward(self, steps: int) -> str:
        while self.curr_page.next and steps > 0:
            self.curr_page = self.curr_page.next
            steps -=1
        return self.curr_page.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)