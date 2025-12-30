"""
Stack Implementation Exercise

Implement a Stack class with the following methods:
- push(item): Add item to top of stack
- pop(): Remove and return top item (raise IndexError if empty)
- peek(): Return top item without removing (raise IndexError if empty)
- is_empty(): Return True if stack is empty
- size(): Return number of items in stack

Hints:
- Use a list as your internal storage
- Top of stack = end of list (most efficient)
- O(1) for all operations

Time limit: 25 minutes
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items[-1]
        del self.items[-1]
        return item

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        if not self.items:
            return True
        return False

    def size(self):
        return len(self.items)


# ============== TESTS ==============
if __name__ == "__main__":
    s = Stack()

    # Test is_empty on new stack
    assert s.is_empty(), "New stack should be empty"
    assert s.size() == 0, "New stack size should be 0"

    # Test push and size
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.size() == 3, "Size should be 3 after 3 pushes"
    assert not s.is_empty(), "Stack should not be empty"

    # Test peek
    assert s.peek() == 30, "Peek should return 30"
    assert s.size() == 3, "Peek should not change size"

    # Test pop
    assert s.pop() == 30, "Pop should return 30"
    assert s.pop() == 20, "Pop should return 20"
    assert s.size() == 1, "Size should be 1 after 2 pops"

    # Test pop remaining
    assert s.pop() == 10, "Pop should return 10"
    assert s.is_empty(), "Stack should be empty"

    # Test error handling
    try:
        s.pop()
        assert False, "pop() on empty stack should raise IndexError"
    except IndexError:
        pass

    try:
        s.peek()
        assert False, "peek() on empty stack should raise IndexError"
    except IndexError:
        pass

    print("All tests passed!")
