#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        # TO-DO: implement this
        self.MAX_CAP = capacity
        self._front = ''
        self._rear = ''
        self.buffer = []

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''

        # TO-DO: implement this

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        return len(self.buffer).
        # TO-DO: implement this
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        # TO-DO: implement this

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        self.buffer.insert(0, x)        # Insert the value at the start of self.buffer

        # AUTO DEQUEUE
        if len(self.buffer) > capacity:     # Check if self.buffer is at max capacity
            self.buffer.pop(capacity)       # If so, pop the end to maintain the capacity

    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        self.buffer.pop(len(self.buffer))   # Remove the last (oldest) value in self.buffer

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        # TO-DO: implement this


class RingBufferFull(Exception):
    '''
    The exception raised when the ring buffer is full when attempting to
    enqueue.
    '''
    pass

class RingBufferEmpty(Exception):
    '''
    The exception raised when the ring buffer is empty when attempting to
    dequeue or peek.
    '''
    pass
