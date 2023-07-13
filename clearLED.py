import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 150)
pixels[0] = (0,0,0)
