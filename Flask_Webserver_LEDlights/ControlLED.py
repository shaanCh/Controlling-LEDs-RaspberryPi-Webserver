#!usr/bin/env/python3

from flask import Flask, render_template, session, request, redirect, url_for
import board
import neopixel
import time
from rpi_ws281x import *
import argparse

app = Flask(__name__)

#LED strip configuration:
LED_COUNT      = 150     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
strip.begin()

def ledcolor(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		color = request.form["color"]
		if color == "red": 
			ledcolor(strip, Color(255,0,0))
			return render_template("ledbutton.html")
		if color == "clearLED":
			ledcolor(strip, Color(0,0,0))
			return render_template("ledbutton.html")
		if color == "orange":
			ledcolor(strip, Color(255,165,0))
			return render_template("ledbutton.html")
		if color == "yellow":
			ledcolor(strip, Color(255,255,0))
			return render_template("ledbutton.html")
		if color == "green":
			ledcolor(strip, Color(0,255,0))
			return render_template("ledbutton.html")
		if color == "blue":
			ledcolor(strip, Color(0,0,255))
			return render_template("ledbutton.html")
		if color == "violet":
			ledcolor(strip, Color(255,0,255))
			return render_template("ledbutton.html")
		if color == "gold":
			ledcolor(strip, Color(218,165,32))
			return render_template("ledbutton.html")
	else:
		return render_template("ledbutton.html")


if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    
