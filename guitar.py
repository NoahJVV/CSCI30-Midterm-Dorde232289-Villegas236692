#!/usr/bin/env python3
'''
	This is a class that defines and tests the guitar.
	
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

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys
import math

if __name__ == '__main__':
  stdkeys.create_window()

  keyboard = "q2we4r5ty7u8i9op-[=]l;'"        # Initialize the keys of the keyboard being used
  samples = []                                # Initialize the samples list

  n_iters = 0
  while True:
    # it turns out that the bottleneck is in polling for key events
    # for every iteration, so we'll do it less often, say every 
    # 1000 or so iterations
    if n_iters == 1000:
        stdkeys.poll()
        n_iters = 0
    n_iters += 1

    # Check if the user has pressed a key. If so, process it:
    if stdkeys.has_next_key_typed():
      new = True                      # Boolean based on if the sample received is new
      key = stdkeys.next_key_typed()  # Assign the keypress to a variable (string)

      # Try-exception block to avoid the RingBufferEmpty exception
      try:
        i = keyboard.index(key)             # Check if the key pressed is in the assigned keyboard
        hertz = 440 * 1.059463 ** (i-12)    # Get the hertz of the sample based on the input key
        capacity = math.ceil(44100/hertz)   # Get the capacity of the RingBuffer

        # Run through all the samples
        for j in samples:
          # Check if the freq. of the sample is equal to the
          # freq. of the sample assigned to the key pressed,
          # reset the freq. of the sample and repluck it
          if j.getCapacity() == capacity:
            j.reset()
            j.pluck()

            # If the sample is not new, break off from the loop
            new = False
            break
        
        # If the sample is new, append the sample to the list of samples
        if new:
          samples.append(GuitarString(hertz))
          samples[len(samples)-1].pluck()
      except:
        pass
    
    # Compute the superposition of the sample to be played
    sample = 0
    for i in samples:
      sample += i.sample()

    # Play the sample on standard audio
    play_sample(sample)

    # Advance the simulation of the guitar string played by one step
    for i in samples:
      i.tick()

      # If the tick surpasses 40000, cut it off
      if i.time() > 40000:
        samples.remove(i)