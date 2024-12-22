class CircularBufferList:
    class __Item:
        def __init__(self, content, next_item=None):
            self.__next_item = next_item
            self.__content = content

        def content(self):
            return self.__content

        def next_item(self):
            return self.__next_item

        def set_next_item(self, item):
            self.__next_item = item

    def __init__(self, size: int):
        self.size: int = size
        self.head: CircularBufferList.__Item = None
        self.tail: CircularBufferList.__Item = None
        self.items_count: int = 0

    def enqueue(self, item):
        if item is None:
            raise ValueError("Cant't enqueue \"None\"!")

        new_item = self.__Item(item, None)
        if not self.head:
            self.head = new_item
            self.tail = new_item
            self.items_count += 1
        else:
            if self.items_count == self.size:
                self.head = self.head.next_item()
            else:
                self.items_count += 1

            self.tail.set_next_item(new_item)
            self.tail = new_item

    def dequeue(self):
        if self.items_count == 0:
            raise IndexError('Buffer is empty!')

        item = self.head
        self.head = item.next_item()
        self.items_count -= 1
        return item.content()

    def peek(self):
        if self.items_count == 0:
            raise IndexError('Buffer is empty!')

        return self.head.content()

    def is_empty(self):
        return self.items_count == 0

    def is_full(self):
        return self.items_count == self.size
