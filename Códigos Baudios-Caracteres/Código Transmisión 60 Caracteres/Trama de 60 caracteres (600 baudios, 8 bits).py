import machine
import utime
from machine import Pin, UART
led = machine.Pin("LED", machine.Pin.OUT)
# parity=0    -> con paridad par (660 bits totales)
# parity=None -> sin paridad (600 bits totales)
uart = UART(0, baudrate=600, bits=8, parity=0, tx=Pin(0), rx=Pin(1))

trama = "A" * 60  # secuencia de 60 caracteres ASCII

while True:
    led.on()
    uart.write(trama)
    utime.sleep(2)
    led.off()
    utime.sleep(2)