from is_even import isEven, is_even
from circular_buffers import CircularBuffer

print(is_even(2), is_even(3), is_even(36), is_even(35))
print(isEven(2), isEven(3), isEven(36), isEven(35))

buffer = CircularBuffer(4)
for i in range(2, 6):
    buffer.enqueue(i)
print(buffer)

for i in range(7, 9):
    buffer.enqueue(i)
print(buffer.dequeue(), buffer)
print(buffer.dequeue(), buffer, '\n')
print(buffer)

print(buffer.dequeue(), buffer)
print(buffer.dequeue(), buffer)
buffer.enqueue(4)
buffer.enqueue(6)
print(buffer.dequeue())
buffer.enqueue(7)
print(buffer)
print('\n\n')

for i in range(2, 5):
    buffer.enqueue(i)
print(buffer)

for i in range(17, 19):
    buffer.enqueue(i)
print(buffer)
print(buffer.dequeue(), buffer)
print(buffer.dequeue(), buffer)
print(buffer.dequeue(), buffer)
print(buffer.dequeue(), buffer, '\n')

for i in range(6, 10):
    buffer.enqueue(i)
print(sum(buffer))

