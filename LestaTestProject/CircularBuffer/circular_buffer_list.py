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
        self.__size = size
        self.__items_count = 0

        self.__head = CircularBuffer.__Item(None, None)
        self.__tail = self.__head
        for i in range(1, self.__size):
            new_item = CircularBuffer.__Item(None, None)
            self.__tail.set_next_item(new_item)
            self.__tail = new_item
        self.__tail.set_next_item(self.__head)
        self.__tail = self.__head

    def __str__(self):
        result = ''
        item = self.__head
        for i in range(self.__size):
            result += f'{i} {item}\n'
            item = item.next_item()
        return result

    def enqueue(self, item):
        if item is None:
            raise ValueError("Cant't enqueue \"None\"!")

        if self.__items_count == self.__size:
            self.__head = self.__head.next_item()
        else:
            self.__items_count += 1

        self.__tail.set_content(item)
        self.__tail = self.__tail.next_item()

    def dequeue(self):
        if self.__items_count == 0:
            raise IndexError('Buffer is empty!')

        content = self.__head.content()
        self.__head.set_content(None)
        self.__head = self.__head.next_item()
        self.__items_count -= 1
        return content

    def peek(self):
        if self.__items_count == 0:
            raise IndexError('Buffer is empty!')

        return self.__head.content()

    def is_empty(self):
        return self.__items_count == 0

    def is_full(self):
        return self.__items_count == self.__size
