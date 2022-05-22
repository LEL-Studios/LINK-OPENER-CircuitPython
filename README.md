# 🔗 LINK-OPENER-CircuitPython
A link opener library for circuitpython boards. This only works with US-Layout keyboards!

# 💾 Installation 
1. Install CircuitPython on your board, use this link: https://circuitpython.org/downloads. Choose your board, for me it was the Raspberry Pi Pico, but it may be different for you.
2. Install the CircuitPython HID Driver, you can use the CircuitPython Driver in this repository under the `lib` folder or you can download it from: https://circuitpython.org/libraries. If you downloaded the bundle, you have to scroll down till you find a folder name `adafruit_hid` and `hid.mpy`. Then place the files under the lib folder.
3. Download this repository, then place the `code.py` file in the root of you board.
4. Go to the `lib` folder and find `golink.py`, place that file in the root of your board.
5. If you want to make your own `code.py` file you can do this: <br>
<br>
```
from golink import golink

golink("https://google.com") # Replace the URL with your own.



...
```

# 📟 LICENSE
```
All code and files in this directory and in directories further down the directory tree is licensed under the MIT License, unless otherwise specified (see below), the whole license and copyright holder(s) is in ./LICENSE.

You shall follow all the terms of the MIT License (./LICENSE) and/or other licenses for the files in this directory.
```

Unless specified otherwise (see below), the license and copyright information applies to all files in this repository.

Individual files may include additional copyright holders. Licenses for the other files can be referred to in the `./credits` folder. 

```
./ (MIT)
    /lib
        /adafruit_hid (MIT, ./credits/Adafruit_CircuitPython_HID)
        hid.mpy (MIT, ./credits/Adafruit_CircuitPython_HID)
```

---

# 📫 Contact
Contact information in GitHub Profile.

