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

from ringbuffer import *
import math
import random

class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        '''
        self.capacity = math.ceil(44100 / frequency)
        self.buffer = RingBuffer(self.capacity)
        self.ticks = 0

    @classmethod
    def make_from_array(cls, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        # Fill buffer with white noise
        for i in range(self.capacity):
            self.buffer.enqueue(random.uniform(-0.5, 0.5))

    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        # Apply Karplus--Strong
        self.buffer.enqueue(0.996 * (0.5 * (self.buffer.dequeue() + self.buffer.peek())))
        # Add a tick count
        self.ticks += 1


    def sample(self) -> float:
        '''
        Return the current sample
        '''
        return self.buffer.peek()

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        return self.ticks
    
    def reset(self):
        self.ticks = 0
        self.buffer.reset()