#!/usr/bin/env python3
'''
	This is a class that defines the ring buffer.
	
	@author Andre Benedict A. Dorde (232289)
	@author Noah Jacob V. Villegas(236692)
	@version 30 September 2024
	
	I have not discussed the Python language code in my program 
	with anyone other than my instructor or the teaching assistants 
	assigned to this course.

	I have not used Python language code obtained from another student, 
	or any other unauthorized source, either modified or unmodified.

	If any Python language code or documentation used in my program 
	was obtained from another source, such as a textbook or website, 
	that has been clearly noted with a proper citation in the comments 
	of my program.
'''

class RingBuffer:
    def __init__(self, capacity: int):
        '''
            Create an empty ring buffer, with given max capacity
        '''
        self.MAX_CAP = capacity             # Initialize the variable stores the max capacity of the ring buffer
        self._front = 0                     # Initialize the variable that stores the index of the front of the ring buffer
        self._rear = 0                      # Initialize the variable that stores the index of the rear of the ring buffer
        self.buffer = [None]*capacity       # Initialize the ring buffer in the form of a list of Nones based on the capacity provided

    def size(self) -> int:
        '''
            Return number of items currently in the buffer
        '''
        count = 0   # Variable that counts the number of items that are not equal to None in the buffer
        for element in self.buffer:
            if element is not None: count += 1

        # Return the count
        return count                                     
    
    def is_empty(self) -> bool:
        '''
            Is the buffer empty (size equals zero)?
        '''
        # Return bool about if buffer is empty
        for element in self.buffer:
            if element is not None: return False
        return True
        
    def is_full(self) -> bool:
        '''
            Is the buffer full (size equals capacity)?
        '''
        # Return bool about if buffer is at full capacity
        for element in self.buffer:
            if element is None: return False
        return True

    def enqueue(self, x: float):
        '''
            Add item `x` to the end
        '''
        # Raise the RingBufferFull exception if the buffer is full already
        if self.is_full(): 
            raise RingBufferFull
        
        # Assign the value that is being queued and
        # update the value for the rear of the buffer
        self.buffer[self._rear] = x                       
        self._rear += 1                                         

        # Wrap around for self._rear
        if self._rear == self.MAX_CAP: self._rear = 0

    def dequeue(self) -> float:
        '''
            Return and remove item from the front
        '''
        # Raise the RingBufferEmpty exception if the buffer is in fact empty
        if self.is_empty():
            raise RingBufferEmpty                              
        
        # Save the value of the item at the front of the buffer to return later
        old_front = self.buffer[self._front]

        # Remove the value that is being dequeued and
        # update the value for the front of the buffer
        self.buffer[self._front] = None
        self._front += 1

        # Wrap around for self._front
        if self._front == self.MAX_CAP: self._front = 0

        # Return the value of the item dequeued
        return old_front

    def peek(self) -> float:
        '''
            Return (but do not delete) item from the front
        '''
        # Raise the RingBufferEmpty exception if the buffer is in fact empty
        if self.is_empty():
            raise RingBufferEmpty
            
        # Return the last (newest) value in self.buffer
        return self.buffer[self._front]

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