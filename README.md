# Controlling WS2812b LED lights using Flask webserver with Raspberry Pi!

## REQUIREMENTS
### Hardware
- Raspberry PI (3 or later recommended)
- WS2812b LED Lights (30pixels/m, 150 LEDs) [Amazon](https://www.amazon.com/gp/product/B00ZHB9M6A?camp=1789&creativeASIN=B00ZHB9M6A&ie=UTF8&linkCode=xm2&tag=temposlight0a-20&th=1)
- 5V 10a Power Supply [Amazon](https://www.amazon.com/gp/product/B0852HL336?camp=1789&creativeASIN=B078RT3ZPS&ie=UTF8&linkCode=xm2&tag=temposlight0a-20&th=1)- comes with a DC Barrel Jack to 2-Pin Terminal Block Adapter
- Male-to-female jumper wire connectors for connecting GPIO pins to LEDs

### Software
**I recommend making a new directory for this project and activating a virtual environment for all the packages**</br>
</br>
Make sure you `sudo apt update` and `sudo apt upgrade`</br>
Also, make sure pip is up to date otherwise you will have package issues `pip install --upgrade pip`</br>
***Python version must be above 3.6*** -check what python version you have with `python3 --version` in the terminal</br>
</br>
These are the packages you will be installing:
- `sudo pip3 install rpi_ws281x`
- `sudo pip3 install adafruit-circuitpython-neopixel`
</br>
If there's an error try pip instead of pip3 otherwise everything should be good to go
</br>

## WS2812b LED Lights
Every type of WS2812b LED lights take **5V**
</br>
Each Pixel on the Strip has 3 individual LEDs for Red, Green, and Blue which each take up **20miliamps** at max brightness
</br></br>
This project requires:
- 9amps = 0.06amps x 150 LEDS
- 5v

Choose your power supply based on the number of LEDs</br>
General Tip: 30pixels/m have LEDS much more spread out per meter than 60pixels/m

## Hardware Connections
1. Connect the negative(white) and the positive(red) wire to the DC barrel jack and screw it down -the jack should have (+) and (-) labels to ensure you are putting wires in the right terminal
2. Connect the male side of the white jumper wire to the white wire port of the LED strip
3. Connect the male side of the green jumper wire to the green wire port of the LED strip
<img src="https://github.com/shaanCh/Controlling-Ws2812bLEDs-RaspberryPi/assets/69170712/73e0f5c3-88a9-4509-9c7a-8eb775af6fd2" width=40% height=30%></br>
4. Connect the female side of the white jumper wire to the ground pin of the Raspberry Pi (Physical Pin #6)
5. Connect the female side of the green jumper wire to GPIO pin number 18
<center><img src="https://github.com/shaanCh/Controlling-Ws2812bLEDs-RaspberryPi/assets/69170712/1ac52167-ca13-4a0d-86bb-dc7873735d04" width=50% height = 50%></center>
</br>
Notice there is no red wire connected to Raspberry Pi this is because the LED lights are getting power from the 5v power supply instead of the Raspberry Pi

## Setting Up a Flask Webserver
I recommend having basic knowledge of Flask and checking out this [Flask Tutorial on YouTube](https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX)

You can use any editor of your choice, but please ensure it's in the directory you want it to be in. For this project, I kept the Flask script inside the "Flask_Webserver_LEDlights" directory

To set up a basic Flask Webserver:
```ruby
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello home"

if __name___ == "__main__"
    app.run()
  
```
## Controlling the LED Lights

Outside the Flask Directory, I had a different set of scripts that tested the functionality of the GPIO pins and LED strip.
The first way I tested the functionality was with the ***strandtest.py*** script which I got from Core Electronics

Copy and paste the code and try it for yourself!
- Make sure you edit the `LED_COUNT = 150` line to match the number of LEDs you have in your strip
- Make sure `LED_PIN = 18` is the right pin number

This is the original code:
```ruby
#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import argparse

# LED strip configuration:
LED_COUNT      = 30     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            print ('Color wipe animations.')
            colorWipe(strip, Color(255, 0, 0))  # Red wipe
            colorWipe(strip, Color(0, 255, 0))  # Blue wipe
            colorWipe(strip, Color(0, 0, 255))  # Green wipe
            print ('Theater chase animations.')
            theaterChase(strip, Color(127, 127, 127))  # White theater chase
            theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
            print ('Rainbow animations.')
            rainbow(strip)
            rainbowCycle(strip)
            theaterChaseRainbow(strip)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
```

You can customize the while True statement at the end of the script for your personalization</br>
The strandtest.py in this repository has been customized for my liking. Go check it out!

### Neopixel
The neopixel library is a different library to individually customize each pixel on the strip

Neopixel does require root access so make sure you have that

To turn on the first pixel of your strip check out the OneLEDLightup.py script or copy this code:
```ruby
import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 150)

pixels[0] = (255, 20, 20)
time.sleep(5)
pixels[0] = (0,0,0)

```
Make sure `pixels = neopixel.NeoPixel(board.D18, 150)` is the right number pin(D18) and the right number of LEDs (150)
You can change the RBG color values to your choice! 

## Combining Flask and LEDs
Inside your directory:
- Create the Python Script for the Flask web server
- create a templates folder to reference the HTML files
- create a static folder to reference the CSS files

The ***ControlLED.py*** script effectively combines flask and strandtest.py into one but there are a few key components to make correct
1. `color = request.form["color"]` the variable must match the HTML "name" element of the buttons</br>
   For example, color matches the name="color" value
   ```
   <form action="#" method="post">
                <button class="Button" id="red" name="color" value="red" type="submit">Red</button>
        </form>
   ``` 
2. `if color == "red": ` for each "if" statement, color must equal the value element of the HTML file as you can see above

This isn't the most efficient way of handling multiple POST requests especially if you have multiple sources of requests. For this project, it's simple and very easy to learn

An efficient way of handling multiple requests would be an **API**

### Customize your website using HTML and CSS 
This is an example of what my website looked like!

<img src="https://github.com/shaanCh/Controlling-Ws2812bLEDs-RaspberryPi/assets/69170712/2d75ec52-c5eb-4dab-b1cf-ece1578dda55">



### WS2812b LED lights in Action!
<img src="https://github.com/shaanCh/Controlling-Ws2812bLEDs-RaspberryPi/assets/69170712/a91fc182-0ea6-43eb-a8df-45eccc22c6fc" width=50% hedihgt=50%>


### Helpful Links
[Control Multiple Fully-Addressable WS2812B RGB LED Strips with a Raspberry Pi Single Board Computer](https://core-electronics.com.au/guides/raspberry-pi/fully-addressable-rgb-raspberry-pi/)</br>
[Learn to Program Custom LED Lights](https://www.temposlighting.com/guides/how-to-add-custom-leds-to-any-project)</br>
[CONTROLLING WS2812B LEDS WITH A RASPBERRY PI](https://www.thegeekpub.com/16187/controlling-ws2812b-leds-with-a-raspberry-pi/)</br>
[Flask Youtube Tutorials](https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX)</br>
[AdaFruit NeoPixel Github](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel)</br>
[NeoPixel on Raspberry Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage)

