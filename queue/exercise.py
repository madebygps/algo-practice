"""
Queue Implementation Exercise

Implement a Queue class with the following methods:
- enqueue(item): Add item to back of queue
- dequeue(): Remove and return front item (raise IndexError if empty)
- peek(): Return front item without removing (raise IndexError if empty)
- is_empty(): Return True if queue is empty
- size(): Return number of items in queue

Hints:
- Use a list as your internal storage
- Front of queue = index 0, Back = end of list
- enqueue appends, dequeue removes from front
- Consider: list.pop(0) is O(n), but fine for learning

Time limit: 25 minutes
"""


class Queue:
    def __init__(self):
        # TODO: Initialize your storage
        self.items = []

    def enqueue(self, item):
        # TODO: Add item to back
        self.items.append(item)

    def dequeue(self):
        # TODO: Remove and return front item
        item = self.items[0]
        del self.items[0]
        return item

    def peek(self):
        # TODO: Return front item without removing
        return self.items[0]

    def is_empty(self):
        # TODO: Check if empty
        if not self.items:
            return True
        return False

    def size(self):
        # TODO: Return count of items
        return len(self.items)


# ============== TESTS ==============
if __name__ == "__main__":
    q = Queue()

    # Test is_empty on new queue
    assert q.is_empty() == True, "New queue should be empty"
    assert q.size() == 0, "New queue size should be 0"

    # Test enqueue and size
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.size() == 3, "Size should be 3 after 3 enqueues"
    assert q.is_empty() == False, "Queue should not be empty"

    # Test peek (should return first item added)
    assert q.peek() == 10, "Peek should return 10 (first in)"
    assert q.size() == 3, "Peek should not change size"

    # Test dequeue (FIFO order)
    assert q.dequeue() == 10, "Dequeue should return 10 (first in, first out)"
    assert q.dequeue() == 20, "Dequeue should return 20"
    assert q.size() == 1, "Size should be 1 after 2 dequeues"

    # Test dequeue remaining
    assert q.dequeue() == 30, "Dequeue should return 30"
    assert q.is_empty() == True, "Queue should be empty"

    # Test error handling
    try:
        q.dequeue()
        assert False, "dequeue() on empty queue should raise IndexError"
    except IndexError:
        pass

    try:
        q.peek()
        assert False, "peek() on empty queue should raise IndexError"
    except IndexError:
        pass

    # Test interleaved operations
    q.enqueue("a")
    q.enqueue("b")
    assert q.dequeue() == "a"
    q.enqueue("c")
    assert q.dequeue() == "b"
    assert q.dequeue() == "c"
    assert q.is_empty() == True

    print("All tests passed!")
