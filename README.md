Queue Implementation Program
Overview
This program demonstrates a flexible queue implementation in Python that allows changing the underlying data structure at runtime. The queue interface supports basic operations such as adding, getting, removing, and clearing elements, as well as dynamically swapping the implementation.

Classes
QueueImpl
An abstract base class defining the interface for queue implementations. It includes the following abstract methods:

add(value): Enqueues an element.
get(): Returns the element expected for FIFO order.
remove(): Dequeues an element.
size(): Returns the number of elements in the queue.
clear(): Removes all elements from the queue.
ListQueue
A concrete implementation of QueueImpl using a list. It provides the required methods to manage the queue operations.

DequeQueue
A concrete implementation of QueueImpl using a deque from the collections module. It provides the required methods to manage the queue operations.

Queue
The main queue class that uses a QueueImpl for its operations. It includes methods to:

add(value): Enqueue an element.
get(): Get the front element without removing it.
remove(): Dequeue the front element.
size(): Get the number of elements in the queue.
clear(): Clear all elements from the queue.
changeImpl(new_impl): Change the underlying implementation at runtime, preserving the FIFO order.