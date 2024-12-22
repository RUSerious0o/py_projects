class CircularBuffer:
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        self.index = 0
        self.items_count = 0

    def __str__(self):
        return f'{self.buffer}, items: {self.items_count}'

    def __iter__(self):
        return iter(self.buffer)

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

        result_index = (self.index + self.size - self.items_count) % self.size
        result = self.buffer[result_index]
        self.buffer[result_index] = None
        self.items_count -= 1
        return result

    def peek(self):
        pass

    def is_empty(self):
        return all(x is None for x in self.buffer)

    def is_full(self):
        return None not in self.buffer
