# play all of the syn6988 sounds with a 2s pause between
# do not use for annoying purposes (unless really justified)
# scruss, 2023-06

import time
import machine
import syn6988

### setup device
ser = machine.UART(
    0, baudrate=9600, bits=8, parity=None, stop=1
)  # tx=Pin(0), rx=Pin(1)

busyPin = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
sp = syn6988.SYN6988(ser, busyPin)


for r in ((101, 124), (201, 209), (301, 318), (401, 408)):
    for s in range(r[0], r[1]+1):
        playstr = "[x1]sound%3d" % s
        print(playstr)
        sp.speak(playstr)
        time.sleep(2)
        

