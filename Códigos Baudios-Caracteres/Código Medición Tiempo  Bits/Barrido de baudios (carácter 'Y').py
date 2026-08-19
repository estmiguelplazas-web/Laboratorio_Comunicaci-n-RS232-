import machine
import utime
from machine import Pin, UART

led = machine.Pin("LED", machine.Pin.OUT)
# baudrate modificado en cada prueba: 1200 / 4800 / 9600 / 38400 / 57600 / 115200
uart = UART(0, baudrate=115200, bits=8, parity=None, tx=Pin(0), rx=Pin(1))

while True:
    led.on()
    uart.write("Y")
    utime.sleep(1)
    led.off()
    utime.sleep(1)