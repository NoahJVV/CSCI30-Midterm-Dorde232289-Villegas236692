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
        self._rear = 0                      # Initialize the variable that stores the rear of the ring buffer
        self.buffer = []                    # Initialize the ring buffer in the form of a list

    def size(self) -> int:
        '''
            Return number of items currently in the buffer
        '''
        return len(self.buffer)                                     # Return the length of the buffer which denotes how many items are in the buffer because we use .pop() and .insert() to add and remove items

    def is_empty(self) -> bool:
        '''
            Is the buffer empty (size equals zero)?
        '''
        return len(self.buffer) == 0                                # Return bool about if buffer is empty
        
    def is_full(self) -> bool:
        '''
            Is the buffer full (size equals capacity)?
        '''
        return len(self.buffer) >= capacity                         # Return bool about if buffer is at full capacity

    def enqueue(self, x: float):
        '''
            Add item `x` to the end
        '''
        try:
            if size(self) >= capacity: 
                raise RingBufferFull                                # Raise exception if buffer is at max capacity

            self.buffer.insert(0, x)                                # Insert the value at the start of self.buffer
            self._front = x                                         # Update the value for the front of the buffer
            self._rear = self.buffer[-1]                            # Update the value for the back of the buffer

            print(f"{x} added. Current size is {size(self)}!")                      # debug, remove after testing

        except:
            print("Ring buffer is full!")

    def dequeue(self) -> float:
        '''
            Return and remove item from the front
        '''
        try:
            if is_empty(self):
                raise RingBufferEmpty                               # Raise exception if buffer is empty

            old_front = self.buffer[0]                              # Save the value of the item at the front of the buffer to return later

            self.buffer.pop(0)                                      # Remove the newest (oldest) value in self.buffer
            self._front = self.buffer[0]                            # Update the value for the front of the buffer
            self._rear = self.buffer[-1]                            # Update the value for the back of the buffer

            return old_front                                        # Return the value of the item removed
        
        except:
            print("Ring buffer is empty!")

    def peek(self) -> float:
        '''
            Return (but do not delete) item from the front
        '''
        try:
            if is_empty(self):
                raise RingBufferEmpty                               # Raise exception if buffer is empty
                
            return self._front                                      # Return the last (newest) value in self.buffer

        except:
            print("Ring buffer is empty!")


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
