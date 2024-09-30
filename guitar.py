#!/usr/bin/env python3
'''
	This is a program that plays notes in the form of guitar strings
  based on the user's input.
	
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
from math import ceil

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    keyboard = "q2we4r5ty7u8i9op-[=]l;'"       # Initialize the keys of the keyboard being used
    samples = []                            # Initialize the samples list

    n_iters = 0
    while True:
      # Polls to wait for user input through key events
      if n_iters == 1000: # Interval at which key events are accepted
        stdkeys.poll()
        n_iters = 0
      n_iters += 1

      # Check if the user has typed a key. If so, process it:
      if stdkeys.has_next_key_typed() :
        key = stdkeys.next_key_typed()  # Assign the key pressed to a variable

        # Avoid accepting weird inputs (SHIFT, CTRL, ALT, NUM LK, etc.)
        if key != '':
          # Try-exception to avoid any sudden exceptions
          try:
            index = keyboard.index(key)       # Assign the index of the key within the keyboard to a var
            new = True                        # Initialize the var that checks whether or not the sample added is new

            # Run through all the samples within the list of samples
            for elem in samples:
              # If the sample's freq. matches the freq. of a sample in the list:
              if elem.buffer.MAX_CAP == ceil(44100 / (440 * 1.059463 ** (index-12))):
                # Pluck the sample
                elem.pluck()

                # Reset the tick count
                elem.ticks = 0

                # Update new to reflect that the sample already exists within the list
                new = False
                break

            # If it is a new sample: 
            if new:
              # Add the sample to the list
              samples.append(GuitarString(440 * 1.059463 ** (index-12)))

              # Pluck the sample
              samples[len(samples)-1].pluck()
          except:
            pass

      # Compute the superposition of samples
      sample = 0
      for i in samples:
        sample += i.sample()

        # Advance the simulation of each guitar string
        i.tick()

        # If the time that the sample has been playing for exceeds the threshold, remove it
        if i.time() > 30000:
          samples.remove(i)
      
      # Play the sample
      play_sample(sample)