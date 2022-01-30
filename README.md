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

```

# 📟 LICENSE

```
MIT License

Copyright(c) 2021 lucaso60 <br>
Copyright(c) 2021 LEL Studios 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
---
Unless specified otherwise (see below), the above license and copyright applies to all files in this repository.

Individual files may include additional copyright holders. Licenses for the other files can be referred to in the `credits` folder. 

```
/ (MIT)
    /lib
        /adafruit_hid (MIT)
        hid.mpy (MIT)
```

# 📫 Contact
You can contact us at dev.lelstudios@outlook.com

