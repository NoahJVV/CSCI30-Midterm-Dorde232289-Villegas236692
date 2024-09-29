#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    keyboard = "q2we4r5ty7u8i9op-[=]"        # Initialize the keys of the keyboard being used
    samples = []                                # Initialize the samples list

    n_iters = 0

    for i in range(len(keyboard)):
            samples.append(GuitarString(440 * 1.059463 ** (i - 12)))
    print(samples)

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

            # If the key exists in the keyboard set, process it
            if keyboard.find(key) != -1:
                index = keyboard.find(key)

                samples[index].pluck()

                for i in samples[index].pluck()
                
        sample = samples[index].sample()

        play_sample(sample)

        samples[index].tick()