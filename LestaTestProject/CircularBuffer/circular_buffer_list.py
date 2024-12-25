class CircularBuffer:
    class __Item:
        def __init__(self, content, next_item=None):
            self.__next_item = next_item
            self.__content = content

        def __str__(self):
            return f'Content: {self.__content}, next: {self.__next_item.__class__}'

        def content(self):
            return self.__content

        def next_item(self):
            return self.__next_item

        def set_next_item(self, item):
            self.__next_item = item

        def set_content(self, content):
            self.__content = content

    def __init__(self, size: int):
        self.size = size
        self.head = CircularBuffer.__Item(None, None)
        self.tail = self.head
        for i in range(1, self.size):
            new_item = CircularBuffer.__Item(None, None)
            self.tail.set_next_item(new_item)
            self.tail = new_item
        self.tail.set_next_item(self.head)
        self.tail = self.head

        self.items_count: int = 0

    def __str__(self):
        result = ''
        item = self.head
        for i in range(self.size):
            result += f'{i} {item}\n'
            item = item.next_item()
        return result

    def enqueue(self, item):
        if item is None:
            raise ValueError("Cant't enqueue \"None\"!")

        if self.items_count == self.size:
            self.head = self.head.next_item()
        else:
            self.items_count += 1

        self.tail.set_content(item)
        self.tail = self.tail.next_item()

    def dequeue(self):
        if self.items_count == 0:
            raise IndexError('Buffer is empty!')

        content = self.head.content()
        self.head.set_content(None)
        self.head = self.head.next_item()
        self.items_count -= 1
        return content

    def peek(self):
        if self.items_count == 0:
            raise IndexError('Buffer is empty!')

        return self.head.content()

    def is_empty(self):
        return self.items_count == 0

    def is_full(self):
        return self.items_count == self.size
