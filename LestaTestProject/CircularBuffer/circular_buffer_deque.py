from collections import deque


class CircularBuffer:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def enqueue(self, item):
        self.buffer.append(item)

    def dequeue(self):
        if not self.buffer:
            raise IndexError("Buffer is empty.")
        return self.buffer.popleft()

    def peek(self):
        if not self.buffer:
            raise IndexError("Buffer is empty.")
        return self.buffer[0]

    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen

    def is_empty(self):
        return len(self.buffer) == 0