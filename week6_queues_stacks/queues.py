# Python program to 
# demonstrate queue implementation
# using list
 
# Initializing a queue
queue = []
 
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
 
print("Initial queue")
print(queue)
 
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
 
print("\nQueue after removing elements")
print(queue)
 
# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty




# deque in Python
from collections import deque
 
# Initializing a queue
q = deque()
 
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
 
print("Initial queue")
print(q)
 
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
 
print("\nQueue after removing elements")
print(q)
 
# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty

q = [1,2,3,4,5,6,7,8,9]





# Python program to
# demonstrate implementation of
# queue using queue module
 
 
from queue import Queue
 
# Initializing a queue
q = Queue(maxsize = 3)
 
# qsize() give the maxsize 
# of the Queue 
print(q.qsize()) 
 
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
 
# Return Boolean for Full 
# Queue 
print("\nFull: ", q.full()) 
 
# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
 
# Return Boolean for Empty 
# Queue 
print("\nEmpty: ", q.empty())
 
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
 
# This would result into Infinite 
# Loop as the Queue is empty. 
# print(q.get())