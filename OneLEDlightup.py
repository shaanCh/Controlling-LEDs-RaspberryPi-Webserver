import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 150)

pixels[0] = (255, 20, 20)
time.sleep(5)
pixels[0] = (0,0,0)
