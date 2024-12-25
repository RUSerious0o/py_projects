class CircularBuffer:
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        self.index = 0
        self.items_count = 0

    def enqueue(self, item) -> None:
        if item is None:
            raise ValueError("Cant't enqueue \"None\"!")

        self.buffer[self.index] = item
        self.index = (self.index + 1) % self.size
        if self.items_count < self.size:
            self.items_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Buffer is empty!')

        item_index = (self.index + self.size - self.items_count) % self.size
        item = self.buffer[item_index]
        self.buffer[item_index] = None
        self.items_count -= 1
        return item

    def peek(self):
        item_index = (self.index + self.size - self.items_count) % self.size
        return self.buffer[item_index]

    def is_empty(self):
        return all(x is None for x in self.buffer)

    def is_full(self):
        return None not in self.buffer
