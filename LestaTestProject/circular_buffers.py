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

        item_index = (self.index + self.size - self.items_count) % self.size
        item = self.buffer[item_index]
        self.buffer[item_index] = None
        self.items_count -= 1
        return item

    def peek(self):
        pass

    def is_empty(self):
        return all(x is None for x in self.buffer)

    def is_full(self):
        return None not in self.buffer


class CircularBufferList:
    class Item:
        def __init__(self, content, next_item):
            self.next_item = next_item
            self.content = content

        def __str__(self):
            return str(self.content)

    def __init__(self, size):
        self.size = size
        self.head = None
        self.tail = None
        self.items_count = 0

    def enqueue(self, item):
        if item is None:
            raise ValueError("Cant't enqueue \"None\"!")

        new_item = self.Item(item, None)
        if not self.head:
            self.head = new_item
            self.tail = new_item
            self.items_count += 1
        else:
            if self.items_count == self.size:
                self.head = self.head.next_item
            else:
                self.items_count += 1

            self.tail.next_item = new_item
            self.tail = new_item

    def dequeue(self):
        if self.items_count == 0:
            raise IndexError('Buffer is empty!')

        item = self.head
        self.head = item.next_item
        self.items_count -= 1
        return item

    def peek(self):
        return self.head

    def is_empty(self):
        return self.items_count == 0

    def is_full(self):
        return self.items_count == self.size
