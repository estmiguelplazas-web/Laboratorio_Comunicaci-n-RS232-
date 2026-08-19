from machine import UART, Pin
import time
# CONFIGURACIÓN UART
uart = UART(
    0,
    baudrate=9600,
    tx=Pin(0),
    rx=Pin(1),
    timeout=1000,
    timeout_char=100
)
# LED integrado
led = Pin("LED", Pin.OUT)
print("TRANSMISOR - PICO")
print("UART: 9600 baudios")
print("TX: GP0")
print("RX: GP1")
print()
print("Sistema listo")
print()
while True:
    # SOLICITAR CARÁCTER
    mensaje = input("Ingrese un carácter: ")
    if len(mensaje) != 1:
        print("ERROR: ingrese solamente un carácter.")
        print()
        continue
    # TRANSMITIR
    uart.write(mensaje + "\n")
    print("Enviado:", mensaje)
    # ESPERAR ACK
    ack_recibido = False
    tiempo_inicio = time.ticks_ms()
    while True:
        if uart.any():
            respuesta = uart.readline()
            if respuesta:
                respuesta = respuesta.decode().strip()
                print("Respuesta recibida:", respuesta)
                # ACK esperado
                if respuesta == "ACK:" + mensaje:
                    ack_recibido = True
                    print("ACK CORRECTO")
                else:
                    print("ACK INCORRECTO")
                break
        if time.ticks_diff(
            time.ticks_ms(),
            tiempo_inicio
        ) > 8000:
            print("TIEMPO DE ESPERA AGOTADO")
            break
    # LED TX
    if ack_recibido:
        print("LED TX: parpadeando durante 3 segundos")
        tiempo_inicio = time.ticks_ms()
        while time.ticks_diff(
            time.ticks_ms(),
            tiempo_inicio
        ) < 3000:
            led.on()
            time.sleep(0.25)
            led.off()
            time.sleep(0.25)
        led.off()
        print("Comunicación exitosa")
    else:
        print("No se pudo confirmar el carácter")
    print()