# Reads Richard Brautigan's famous poem
# scruss, 2023-06

"""
 first edition of this poem can be freely reproduced if no
 money is charged, according to Richard Brautigan's
 mimeographed publication
"""

import machine
import syn6988

poem = [
    "All Watched Over By Machines Of Loving Grace[p100]",
    "by Richard Brautigan[p500]",
    "I like to think (and",
    "the sooner the better!)",
    "of a cybernetic meadow",
    "where mammals and computers",
    "live together in mutually",
    "programming harmony",
    "like pure water",
    "touching clear sky.",
    "[p300]",
    "I like to think",
    "(right now, please!)",
    "of a cybernetic forest",
    "filled with pines and electronics",
    "where deer stroll peacefully",
    "past computers",
    "as if they were flowers",
    "with spinning blossoms.",
    "[p300]",
    "I like to think",
    "(it has to be!)",
    "of a cybernetic ecology",
    "where we are free of our labors",
    "and joined back to nature,",
    "returned to our mammal",
    "brothers and sisters,",
    "and all watched over",
    "by machines of loving grace.",
]

ser = machine.UART(
    0, baudrate=9600, bits=8, parity=None, stop=1
)  # tx=Pin(0), rx=Pin(1)

busy = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
s = syn6988.SYN6988(ser, busy)


s.speak("[x1]soundy[d][p500]")
s.speak("[t3][s6]")
for p in poem:
    print(p)
    s.speak(p)
s.speak("[p500][x1]soundy[d][s6]")
