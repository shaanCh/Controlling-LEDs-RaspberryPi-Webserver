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
</br>
## Hardware Connections

### Customize your website using HTML and CSS 
![LEDwebsite](https://github.com/shaanCh/Fun/assets/69170712/e0184fa4-b346-4c55-a88f-fa7909be7b54.png)



### WS2812b LED lights in Action!
![ledlights](https://github.com/shaanCh/Fun/assets/69170712/6aa90ce9-0212-430f-a0e0-e38fbc8dfcb8)
