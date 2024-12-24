import unittest
import logging
import time

from is_even import isEven, is_even


class IsEvenTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='is_even_tests.log', filemode='w', encoding='utf-8', level=logging.INFO,
                            format='%(asctime)s | %(levelname)s | %(message)s')
        cls.ITERATIONS = 10_000_000
        cls.START_VALUE = 10 ** 100

    def execution_time_measure(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            logging.info(f'Время выполнения {func.__name__}: {time.time() - start: .5f} сек.')

        return wrapper

    @execution_time_measure
    def test_isEven(self):
        self.assertEqual(isEven(3), False)
        self.assertEqual(isEven(4), True)
        for i in range(self.START_VALUE, self.START_VALUE + self.ITERATIONS):
            is_even(i)

    @execution_time_measure
    def test_is_even(self):
        self.assertEqual(is_even(3), False)
        self.assertEqual(is_even(4), True)
        for i in range(self.START_VALUE, self.START_VALUE + self.ITERATIONS):
            isEven(i)


if __name__ == '__main__':
    unittest.main()
