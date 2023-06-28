# very crude MicroPython demo of SYN6988 TTS chip
# scruss, 2023-06
# look at the embedded text commands for guidance at
# https://github.com/scruss/micropython-SYN6988
import machine
import syn6988


### setup device
ser = machine.UART(
    0, baudrate=9600, bits=8, parity=None, stop=1
)  # tx=Pin(0), rx=Pin(1)

busyPin = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
s = syn6988.SYN6988(ser, busyPin)


def speak_and_spell(r):
    # print then speak string r
    print(r)
    s.speak(r)


speak_and_spell(
    "[g2]Hello! [g1]你好![g2]"
)  # language selection with [g*]
speak_and_spell("I can speak in English, and also in Chinese:")
speak_and_spell("[g1]千里之行，始于足下。[g2]")
speak_and_spell(
    "which means: a journey of five hundred kilometres starts with the first step"
)
speak_and_spell(
    "[s1]I can speak slowly, [s9] and I can speak very fast[s5]"
)  # speed: [s*]
speak_and_spell(
    "[v5]I can be [v10]loud or [v1]very quiet. [v5]"
)  # volume [v*]
speak_and_spell(
    "I can use [t1]low tones [t5]or [t8]high tones[t5]"
)  # tone [t*]


# turn off blocking mode to speak the last bit
s.block = False
speak_and_spell(
    "[d][g0]my work here is done [x1]soundy[d]"
)  # play a chime with [x1]
print("but I'm still speaking in non-blocking mode")
