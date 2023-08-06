# GPIO CONTROL IN RASPBERRY PI PICO
## Hardware control
### Input Devices
- Touch Sensor
- Potenciometer
- Joystick
- PIR
- LM35
### Ouput Devices
- LED
- Reley
- Solid state relay
- Motor DC
- RGB
- Servo motor


```python
from gpiopico import Led

led1 = Led(2, True)
led1.change_pwm(125) #value 0-255
```