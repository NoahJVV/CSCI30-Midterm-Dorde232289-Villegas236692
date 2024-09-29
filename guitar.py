#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys
from math import ceil

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    keyboard = "q2we4r5ty7u8i9op-[=]"        # Initialize the keys of the keyboard being used
    samples = []                                # Initialize the samples list

    # for i in range(len(keyboard)):
    #   samples.append(GuitarString(440 * 1.059463 ** (i - 12)))
    # print(samples)

    n_iters = 0
    while True:
      # it turns out that the bottleneck is in polling for key events
      # for every iteration, so we'll do it less often, say every 
      # 1000 or so iterations
      if n_iters == 1000:
        stdkeys.poll()
        n_iters = 0
      n_iters += 1

      sample = 0
      index = 0
      # check if the user has typed a key; if so, process it
      if stdkeys.has_next_key_typed():
        key = stdkeys.next_key_typed()
        print(key)
#SpecAccurateNoah basis ends here

        try:
          i = keyboard.index(key)
          new = True
          for j in samples:
            if j.buffer.MAX_CAP == ceil(44100 / (440 * 1.059463 ** (i-12))):
              j.pluck()
              j.ticks = 0
              new = False
              print("Old string plucked\n\n")
              break
          if new:
            samples.append(GuitarString(440 * 1.059463 ** (i-12)))
            samples[len(samples)-1].pluck()
            print("New string plucked\n\n")
        except:
          pass
      
      sample = 0
      for i in samples:
        sample += i.sample()
        i.tick()
        if i.time() > 30000:
          samples.remove(i)
      
      play_sample(sample)
        
#SpecAccurateNoah basis starts here
      #   # If the key exists in the keyboard set, process it
      #   if keyboard.find(key) != -1:
      #     index = keyboard.find(key)

      #     samples[index].pluck()

      # for i in samples:
      #   if i.sample() != 0:
      #     print(f"i-sample: {i.sample()}\n\n")
      #     sample += i.sample()
      #     i.tick()

      # play_sample(sample)