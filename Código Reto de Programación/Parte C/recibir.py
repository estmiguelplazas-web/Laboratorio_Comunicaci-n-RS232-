from machine import UART, Pin, I2C
import ssd1306
import time
# UART
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
# FUNCIÓN PARA ACTUALIZAR OLED
def mostrar_oled(linea_numero, total, estado):
    oled.fill(0)
    oled.text("RECIBIENDO", 0, 0)
    oled.text("ARCHIVO", 0, 10)
    oled.text("Linea: {:04d}".format(linea_numero), 0, 25)
    oled.text(
        "Recibidas: {}".format(total),
        0,
        37
    )
    oled.text(
        "Estado: " + estado,
        0,
        52
    )
    oled.show()
# PANTALLA INICIAL
oled.fill(0)
oled.text("RECEPTOR", 0, 0)
oled.text("PICO 2 W", 0, 12)
oled.text("Esperando...", 0, 30)
oled.text("UART listo", 0, 45)
oled.show()
# CONSOLA
print("          RECEPTOR DE ARCHIVO")
print("UART: 9600 baudios")
print("RX: GP17")
print("TX: GP16")
print("OLED: GP20/GP21")
print()
print("Esperando archivo...")
print()
# CREAR ARCHIVO
archivo = open("recibido.txt", "w")
contador = 0
# RECEPCIÓN
while True:
    if uart.any():
        dato = uart.readline()
        if dato:
            linea = dato.decode().strip()
            if len(linea) > 0:
                contador += 1
                print("Línea recibida:", linea)
                # GUARDAR EN ARCHIVO
                archivo.write(linea + "\n")
                archivo.flush()
                # LED
                led.on()
                time.sleep(0.1)
                led.off()
                # OLED
                # Intentamos extraer el número
                try:
                    numero = int(linea[:4])
                except:
                    numero = contador
                mostrar_oled(
                    numero,
                    contador,
                    "OK"
                )
                # ACK
                uart.write("ACK\n")
                print("ACK enviado")
                print("Líneas recibidas:", contador)
                print()