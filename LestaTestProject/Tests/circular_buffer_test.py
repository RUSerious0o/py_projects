import unittest
import logging
from random import randint
import time

from CircularBuffer.circular_buffer import CircularBuffer as CB_python_list
from CircularBuffer.circular_buffer_list import CircularBuffer as CB_list
from CircularBuffer.circular_buffer_deque import CircularBuffer as CB_deque


class CircularBufferTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='circular_buffer_tests.log', filemode='w', encoding='utf-8', level=logging.INFO,
                            format='%(asctime)s | %(levelname)s | %(message)s')
        cls.BUFFER_SIZE = 9
        cls.DATA = range(2, 14)
        cls.ITERATIONS = 1_500_000

    def execution_time_measure(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            logging.info(f'Время выполнения {func.__name__}: {time.time() - start: .5f} сек.')

        return wrapper

    def CB_test(self, buffer):
        for value in self.DATA:
            buffer.enqueue(value)

        expected_value = 5
        for i in range(self.BUFFER_SIZE - 1):
            self.assertEqual(expected_value, buffer.dequeue())
            expected_value += 1

        self.assertEqual(13, buffer.peek())

        buffer.enqueue(20)
        buffer.enqueue(30)
        self.assertEqual(13, buffer.dequeue())
        self.assertEqual(20, buffer.dequeue())
        self.assertEqual(30, buffer.dequeue())

        self.assertRaises(IndexError, buffer.dequeue)
        self.assertRaises(ValueError, buffer.enqueue, None)

        for value in range(self.ITERATIONS):
            if randint(0, 100) < 30:
                try:
                    buffer.dequeue()
                except IndexError:
                    pass
            else:
                buffer.enqueue(value)

    @execution_time_measure
    def test_CB_python_list(self):
        self.CB_test(CB_python_list(self.BUFFER_SIZE))

    @execution_time_measure
    def test_CB_list(self):
        self.CB_test(CB_list(self.BUFFER_SIZE))

    @execution_time_measure
    def test_CB_deque(self):
        self.CB_test(CB_deque(self.BUFFER_SIZE))


if __name__ == '__main__':
    unittest.main()
