#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys
import math

if __name__ == '__main__':
  stdkeys.create_window()

  keyboard = "q2we4r5ty7u8i9op-[=]"
  samples = []

  n_iters = 0
  while True:
    if n_iters == 1000:
        stdkeys.poll()
        n_iters = 0
    n_iters += 1

    if stdkeys.has_next_key_typed():
      new = True
      key = stdkeys.next_key_typed()
      try:
        i = keyboard.index(key)
        hertz = 440 * 1.059463 ** (i-12)
        capacity = math.ceil(44100/hertz)
        for j in samples:
          if j.getCapacity() == capacity:
            j.reset()
            j.pluck()
            new = False
            break
        if new:
          samples.append(GuitarString(hertz))
          samples[len(samples)-1].pluck()
      except:
        pass
    
    sample = 0
    for i in samples:
      sample += i.sample()

    play_sample(sample)

    for i in samples:
      i.tick()
      if i.time() > 30000:
        samples.remove(i)