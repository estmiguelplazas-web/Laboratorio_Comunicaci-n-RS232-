import machine
import utime
from machine import Pin, UART

led = machine.Pin("LED", machine.Pin.OUT)
uart = UART(0, baudrate=57600, bits=7, parity=0, stop=2, tx=Pin(0), rx=Pin(1))

mensaje = "UMNG LIDER EN INGENIERIA EN TELECOMUNCACIONES"

while True:
    led.on()
    uart.write(mensaje)
    utime.sleep(2)
    led.off()
    utime.sleep(2)