"""
 simple MicroPython sender library
 for YuTone VoiceTX SYN6988 text to speech synthesizer module
 scruss, 2023-06
 -*- coding: utf-8 -*-
"""

import machine
import time


class SYN6988:
    def __init__(self, uart, busyPin, block=True):
        self.uart = uart
        self.busy = machine.Signal(busyPin, invert=False)
        self._block = block

    @property
    def block(self):
        return self._block

    @block.setter
    def block(self, b):
        if b == True:
            self._block = True
        else:
            self._block = False

    def fauxutf16(self, s, badchar=" "):
        # encodes string s as UTF-16BE, two bytes per char, no BOM
        # eg: "hello" => b'\x00h\x00e\x00l\x00l\x00o'
        # char codes > 65535 encoded as badchar
        # MicroPython can only encode to UTF-8 bytes, so we need this
        buf = bytearray(len(s) * 2)  # preallocate empty buffer
        for i, c in enumerate(s):
            n = ord(c)
            if n > 65535:
                n = ord(badchar)
            buf[2 * i] = n // 256
            buf[2 * i + 1] = n % 256
        return bytes(buf)

    def isBusy(self):
        return self.busy.value() == True

    def speak(self, data):
        data_bytes = self.fauxutf16(data)  # returns bytes object
        tx_len = len(data_bytes) + 2
        ## assumes UTF-16BE encoding
        buf = bytes([0xFD, tx_len // 256, tx_len % 256, 0x01, 0x04])
        self.uart.write(buf + data_bytes)
        time.sleep(0.1)  # not quite asserted as busy immediately
        if self.block:
            while self.isBusy():
                pass
