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
        self._front = 0                     # Initialize the variable that stores the front of the ring buffer
        self._rear = 1                      # Initialize the variable that stores the rear of the ring buffer
        self.buffer = [None]*capacity       # Initialize the ring buffer in the form of a list

    def size(self) -> int:
        '''
            Return number of items currently in the buffer
        '''
        count = 0
        for element in self.buffer:
            if element is not None: count += 1

        return count                                     

    def is_empty(self) -> bool:
        '''
            Is the buffer empty (size equals zero)?
        '''
        # Return bool about if buffer is empty
        return self.size() == 0
        
    def is_full(self) -> bool:
        '''
            Is the buffer full (size equals capacity)?
        '''
        return self.size() >= self.MAX_CAP                     # Return bool about if buffer is at full capacity

    def enqueue(self, x: float):
        '''
            Add item `x` to the end
        '''
        try:
            if self.size() >= self.MAX_CAP: 
                raise RingBufferFull                                # Raise exception if buffer is at max capacity 
            
            # Self 
            self.buffer[self._rear] = x                       #
            self._rear += 1                                         #

            if self._rear == self.MAX_CAP: self._rear = 0           #

            # print(f"{self.buffer} LOOK AT ME!!!!!! I AM ADDING!!!!!!!!!!!!!!!!")

        except:
            print(" ")

    def dequeue(self) -> float:
        '''
            Return and remove item from the front
        '''
        try:
            if self.is_empty():
                raise RingBufferEmpty                               # Raise exception if buffer is empty
            
            # print(f"{self.buffer} LOOK AT ME!!!!!! I AM GAMER!!!!!")

            old_front = self.buffer[self._front]                    # Save the value of the item at the front of the buffer to return later

            self.buffer[self._front] = None                         # Remove the value that is being dequeued
            self._front += 1                                        # Update the value for the front of the buffer

            if self._front == self.MAX_CAP: self._rear = 0          #

            return old_front                                        # Return the value of the item removed
        
        except:
            print(" ")

    def peek(self) -> float:
        '''
            Return (but do not delete) item from the front
        '''
        try:
            if self.is_empty():
                raise RingBufferEmpty                               # Raise exception if buffer is empty
                
            return self._front                                      # Return the last (newest) value in self.buffer

        except:
            print(" ")


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
