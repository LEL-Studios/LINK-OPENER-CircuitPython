"""
All code in this file is licensed under the MIT License, the whole license and copyright holder(s) is in ./LICENSE.

You shall follow all the terms of the MIT License (./LICENSE).
"""

import time
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import usb_hid


def golink(link):
    print("Setting up keyboard...")
    kbd = Keyboard(usb_hid.devices)
    time.sleep(0.5)

    kbd.send(Keycode.WINDOWS, Keycode.R)
    kbd.release_all()

    time.sleep(1)

    URL = f"microsoft-edge:{link}"
    for char in URL:
        print(char)
        if char == ":":
            kbd.send(Keycode.SHIFT, Keycode.SEMICOLON)
        elif char == "/":
            kbd.send(Keycode.FORWARD_SLASH)
        elif char == ".":
            kbd.send(Keycode.PERIOD)
        elif char == "?":
            kbd.send(Keycode.SHIFT, Keycode.FORWARD_SLASH)
        elif char == "=":
            kbd.send(Keycode.EQUALS)
        elif char == "-":
            kbd.send(Keycode.MINUS)
        else:
            send(char, kbd)
        kbd.release_all()

    kbd.release_all()

    kbd.send(Keycode.ENTER)
    kbd.release_all()


def send(keycode, kbd):
    if keycode == "a":
        kbd.send(Keycode.A)
    elif keycode == "b":
        kbd.send(Keycode.B)
    elif keycode == "c":
        kbd.send(Keycode.C)
    elif keycode == "d":
        kbd.send(Keycode.D)
    elif keycode == "e":
        kbd.send(Keycode.E)
    elif keycode == "f":
        kbd.send(Keycode.F)
    elif keycode == "g":
        kbd.send(Keycode.G)
    elif keycode == "h":
        kbd.send(Keycode.H)
    elif keycode == "i":
        kbd.send(Keycode.I)
    elif keycode == "j":
        kbd.send(Keycode.J)
    elif keycode == "k":
        kbd.send(Keycode.K)
    elif keycode == "l":
        kbd.send(Keycode.L)
    elif keycode == "m":
        kbd.send(Keycode.M)
    elif keycode == "o":
        kbd.send(Keycode.O)
    elif keycode == "p":
        kbd.send(Keycode.P)
    elif keycode == "q":
        kbd.send(Keycode.Q)
    elif keycode == "r":
        kbd.send(Keycode.R)
    elif keycode == "s":
        kbd.send(Keycode.S)
    elif keycode == "t":
        kbd.send(Keycode.T)
    elif keycode == "u":
        kbd.send(Keycode.U)
    elif keycode == "v":
        kbd.send(Keycode.V)
    elif keycode == "w":
        kbd.send(Keycode.W)
    elif keycode == "x":
        kbd.send(Keycode.X)
    elif keycode == "y":
        kbd.send(Keycode.Y)
    elif keycode == "z":
        kbd.send(Keycode.Z)
    elif keycode == "1":
        kbd.send(Keycode.ONE)
    elif keycode == "2":
        kbd.send(Keycode.TWO)
    elif keycode == "3":
        kbd.send(Keycode.THREE)
    elif keycode == "4":
        kbd.send(Keycode.FOUR)
    elif keycode == "5":
        kbd.send(Keycode.FIVE)
    elif keycode == "6":
        kbd.send(Keycode.SIX)
    elif keycode == "7":
        kbd.send(Keycode.SEVEN)
    elif keycode == "8":
        kbd.send(Keycode.EIGHT)
    elif keycode == "9":
        kbd.send(Keycode.NINE)

    if keycode == "A":
        kbd.send(Keycode.SHIFT, Keycode.A)
    elif keycode == "B":
        kbd.send(Keycode.SHIFT, Keycode.B)
    elif keycode == "C":
        kbd.send(Keycode.SHIFT, Keycode.C)
    elif keycode == "D":
        kbd.send(Keycode.SHIFT, Keycode.D)
    elif keycode == "E":
        kbd.send(Keycode.SHIFT, Keycode.E)
    elif keycode == "F":
        kbd.send(Keycode.SHIFT, Keycode.F)
    elif keycode == "G":
        kbd.send(Keycode.SHIFT, Keycode.G)
    elif keycode == "H":
        kbd.send(Keycode.SHIFT, Keycode.H)
    elif keycode == "I":
        kbd.send(Keycode.SHIFT, Keycode.I)
    elif keycode == "J":
        kbd.send(Keycode.SHIFT, Keycode.J)
    elif keycode == "K":
        kbd.send(Keycode.SHIFT, Keycode.K)
    elif keycode == "L":
        kbd.send(Keycode.SHIFT, Keycode.L)
    elif keycode == "M":
        kbd.send(Keycode.SHIFT, Keycode.M)
    elif keycode == "O":
        kbd.send(Keycode.SHIFT, Keycode.O)
    elif keycode == "P":
        kbd.send(Keycode.SHIFT, Keycode.P)
    elif keycode == "Q":
        kbd.send(Keycode.SHIFT, Keycode.Q)
    elif keycode == "R":
        kbd.send(Keycode.SHIFT, Keycode.R)
    elif keycode == "S":
        kbd.send(Keycode.SHIFT, Keycode.S)
    elif keycode == "T":
        kbd.send(Keycode.SHIFT, Keycode.T)
    elif keycode == "U":
        kbd.send(Keycode.SHIFT, Keycode.U)
    elif keycode == "V":
        kbd.send(Keycode.SHIFT, Keycode.V)
    elif keycode == "W":
        kbd.send(Keycode.SHIFT, Keycode.W)
    elif keycode == "X":
        kbd.send(Keycode.SHIFT, Keycode.X)
    elif keycode == "Y":
        kbd.send(Keycode.SHIFT, Keycode.Y)
    elif keycode == "Z":
        kbd.send(Keycode.SHIFT, Keycode.Z)
