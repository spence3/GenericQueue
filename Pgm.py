from collections import deque
from abc import ABC, abstractmethod


class QueueImpl(ABC):
    @abstractmethod
    def add(self, value):
        pass
    
    def get(self):
        pass

    def remove(self):
        pass

    def size(self):
        pass

    def clear(self):
        pass


class MyList(QueueImpl):
    def __init__(self):
        self.data = []

    def add(self, value):
        """enqueues an element"""
        self.data.append(value)

    def get(self):
        """returns the element expected for FIFO order"""
        return self.data[0] if len(self.data) != 0 else None

    def remove(self):
        """dequeues an element (FIFO order, of course)"""
        self.data.pop(0) if len(self.data) != 0 else None

    def size(self):
        """returns the number of elements in the queue"""
        return len(self.data)

    def clear(self):
        """removes all elements from the queue"""
        self.data = []


class MyDequeue(QueueImpl):
    def __init__(self):
        self.data = deque()
    
    def add(self, value):
        """enqueues an element"""
        self.data.append(value)

    def get(self):
        """returns the element expected for FIFO order"""
        return self.data[0] if len(self.data) != 0 else None

    def remove(self):
        """dequeues an element (FIFO order, of course)"""
        self.data.popleft() if len(self.data) != 0 else None

    def size(self):
        """returns the number of elements in the queue"""
        return len(self.data)

    def clear(self):
        """removes all elements from the queue"""
        self.data = []



class Queue(QueueImpl):
    def __init__(self, impl:QueueImpl):
        impl.data.clear() # clear data before joining with currentImpl
        self.currentImpl = impl

    def add(self, value):
        """enqueues an element"""
        self.currentImpl.add(value)

    def get(self):
        """returns the element expected for FIFO order"""
        return self.currentImpl.get() 

    def remove(self):
        """dequeues an element (FIFO order, of course)"""
        self.currentImpl.remove()

    def size(self):
        """returns the number of elements in the queue"""
        return self.currentImpl.size()

    def clear(self):
        """removes all elements from the queue"""
        self.currentImpl.clear()

    def changeImpl(self, newImpl:QueueImpl):
        """changes implementation of the queue"""
        newImpl.clear()

        while self.size() > 0:
            element = self.get()
            self.remove()
            newImpl.add(element)
        self.currentImpl = newImpl


def displayAndEmptyQueue(q:Queue):
    while q.size() > 0:
        print(q.get(), end=" ")
        q.remove()
    print()



def main():
    # try with ints
    dequeueImpl = MyDequeue()
    q = Queue(dequeueImpl)
    q.add(91)
    q.add(92)

    l = MyList()
    l.add(93)
    q.changeImpl(l)
    q.add(94)
    q.add(95)
    displayAndEmptyQueue(q)

    # try with strings
    dq = MyDequeue()
    dq.add("remove me")
    q2 = Queue(dq)
    q2.add("91")
    q2.add("92")

    l2 = MyList()
    l2.add("93")
    q2.changeImpl(l2)
    q2.add("94")
    q2.add("95")
    displayAndEmptyQueue(q2)

if __name__ == '__main__':
    main()