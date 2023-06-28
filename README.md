# micropython-SYN6988
MicroPython library for the YuTone VoiceTX SYN6988 text to speech module.


## Introduction 

<img src="images/syn6988-front.webp" width="628" height="600"
alt="blue circuit board with central processor chip and audio outputs"
/>

The SYN6988 is one of several speech synthesizer / text-to-speech
(TTS) modules available inexpensively on AliExpress and other
vendors. It's impressive because:

* it produces clear English speech without resorting to phonemes;

* it has a line out / headphone jack and small speaker outputs, both
  featuring very clean audio;
  
* it is easy to interface to, either through asynchronous serial or
  SPI (the latter not attempted here);
  
* it has some flexibility in volume, pitch and rate of speech (but
  it's no [DECtalk](https://github.com/dectalk/dectalk));
  
* it has a large library of alert tones built-n;
  
* it is not expensive, being around 🇨🇦 $15.

Of course, there are downsides:

* all of the documentation *so far* is in Chinese;

* it has only one faintly-accented female voice with a slightly robotic
  delivery;
  
* you may not get the board you ordered! I was sold this board as
  having an XFS5152 chip when it clearly has a SYN6988.
  
## Interfacing

The SYN6988 is a 3.3 V device for both logic and power. It requires a
two-wire UART connection plus an additional digital input pin to
monitor the busy status of the TTS.

        SYN6988        MicroPython Board     Raspberry Pi Pico
	   =========      ===================   ===================
	   
	    RDY            Digital Input         GPIO 2
		RXD            UART TXD              GPIO 0 (UART 0 TX)
		TXD            UART RXD              GPIO 1 (UART 0 RX)
		GND            Ground                Any GND pin
		3V3            3V3 supply            3V3(OUT)
		
The SYN6988 uses a fixed serial port rate defined by the arrangement
of resistors in the serial speed selection block. Mine is hard-wired
for 9600 baud.

For a Raspberry Pi Pico, these connections might be supported in code
with:

```python3
ser = machine.UART(0, baudrate=9600, bits=8, parity=None, stop=1)
busyPin = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

```

Audio output is either through the headphone / line out jack or via
the speaker pins. This output is unamplified. I can drive a very small
oval speaker at a comfortable volume from the speaker pins, but large
heaphones can be very quiet.

The board I have is not remotely breadboard-friendly. I solved that by
taking two 6-pin Arduino stacking headers, bending the pins out and
back in at right angles, then gluing the two headers back to
back. This gives a header block that bridges the central trough in a
breadboard, allowing the SYN6988 board to sit centrally.

<img src="images/syn6988_pico.jpg" width="1045" height="1045"
alt="SYNC6988 with Raspberry Pi Pico and small speaker" />

## Operation

If the board is connected correctly, the red Ready LED will be lit
when the TTS is not speaking. This LED will go out when the TTS is
speaking, and the RDY pin will go low shortly (about 0.1 s) after the
speech starts, and go high when speech is finished.

If the initialization code above is used, the following MicroPython
will speak a rather quiet "Hello" from the board:

```python3
import syn6988

s = syn6988.SYN6988(ser, busyPin)
s.speak("[v1]hello")
```

