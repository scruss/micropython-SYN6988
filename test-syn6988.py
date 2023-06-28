# very crude MicroPython sender for SYN6988
# scruss, 2023-06
import time
import machine
import syn6988


ser = machine.UART(
    0, baudrate=9600, bits=8, parity=None, stop=1
)  # tx=Pin(0), rx=Pin(1)

busyPin = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
s = syn6988.SYN6988(ser, busyPin)

s.speak("[v1]hello")

# "a journey of five hundred kilometres starts with the first step"
#s.speak("[v1][g1]千里之行，始于足下。[d]")
# s.speak("[t1]ha [t3]ha [t5]ha [t7]ha [t9]ha ")
# s.speak("[s0]faster and [s1]faster and [s2]faster and [s3]faster and [s4]faster and [s5]faster and [s6]faster and [s7]faster and [s8]faster and [s9]faster and [s10]faster")
s.block = False
s.speak('this is just to say that ...')
s.speak("[d][g0][v1]my work here is done [x1]soundy[d]")
print(" am I still speaking?")
print(s.block)
