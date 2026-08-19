import machine
import utime
from machine import Pin, UART

led = machine.Pin("LED", machine.Pin.OUT)
# parity=None -> sin paridad
# parity=0    -> con paridad par (prueba original)
# parity=1    -> con paridad impar (variante modificada)
uart = UART(0, baudrate=115200, bits=7, parity=0, tx=Pin(0), rx=Pin(1))

while True:
    led.on()
    uart.write("-")
    utime.sleep(1)
    led.off()
    utime.sleep(1)