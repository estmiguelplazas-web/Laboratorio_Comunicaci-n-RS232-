from machine import UART, Pin, I2C
import ssd1306
import time
# CONFIGURACIÓN UART
uart = UART(
    0,
    baudrate=9600,
    tx=Pin(16),
    rx=Pin(17),
    timeout=1000,
    timeout_char=100
)
# LED
led = Pin("LED", Pin.OUT)
# OLED SSD1306
i2c = I2C(
    0,
    scl=Pin(21),
    sda=Pin(20),
    freq=400000
)
oled = ssd1306.SSD1306_I2C(
    128,
    64,
    i2c
)
# PANTALLA INICIAL
oled.fill(0)
oled.text("RECEPTOR", 0, 0)
oled.text("PICO 2 W", 0, 12)
oled.text("Esperando...", 0, 30)
oled.text("UART listo", 0, 45)
oled.show()
# CONSOLA
print("        RECEPTOR - PICO 2 W")
print("UART: 9600 baudios")
print("RX: GP17")
print("TX: GP16")
print("OLED:")
print("SDA: GP20")
print("SCL: GP21")
print()
print("Sistema listo")
print()
# RECEPCIÓN
while True:
    if uart.any():
        dato = uart.readline()
        if dato:
            mensaje = dato.decode().strip()
            if len(mensaje) == 0:
                continue
            # MOSTRAR EN CONSOLA
            print("Carácter recibido:", mensaje)
            # MOSTRAR EN OLED
            oled.fill(0)
            oled.text("CARACTER", 0, 0)
            oled.text("RECIBIDO", 0, 10)
            oled.text(
                "Dato: " + mensaje,
                0,
                30
            )
            oled.text(
                "Procesando...",
                0,
                45
            )
            oled.show()
            # LED RX - 5 SEGUNDOS
            print("LED RX encendido durante 5 segundos")
            led.on()
            time.sleep(5)
            led.off()
            print("LED RX apagado")
            # ENVIAR ACK
            respuesta = "ACK:" + mensaje
            uart.write(respuesta + "\n")
            print(
                "ACK enviado:",
                respuesta
            )
            # OLED - CONFIRMACIÓN
            oled.fill(0)
            oled.text("CARACTER", 0, 0)
            oled.text("RECIBIDO", 0, 10)
            oled.text(
                "Dato: " + mensaje,
                0,
                30
            )
            oled.text(
                "ACK enviado",
                0,
                45
            )
            oled.show()
            print("Comunicación confirmada")
            print()