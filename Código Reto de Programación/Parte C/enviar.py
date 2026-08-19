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
print("       ENVÍO Y MEDICIÓN DE ARCHIVO")
print("UART: 9600 baudios")
print("TX: GP0")
print("RX: GP1")
print()
# INTERVALO
while True:
    try:
        intervalo = float(
            input("Intervalo entre líneas (segundos): ")
        )
        if intervalo >= 0:
            break
        print("ERROR: el intervalo no puede ser negativo.")
    except ValueError:
        print("ERROR: introduzca un número válido.")
# ABRIR ARCHIVO
try:
    archivo = open("alfabetos.txt", "r")
except OSError:
    print("ERROR: no se encontró alfabetos.txt")
    print("Ejecute primero generadortxt.py.")
    while True:
        pass
# INICIO DE LA TRANSFERENCIA
contador = 0
print()
print("Preparando transmisión...")
time.sleep(1)
print("INICIO DE LA TRANSFERENCIA")
print()
tiempo_inicio = time.ticks_ms()
# TRANSMISIÓN
for linea in archivo:
    linea = linea.strip()
    if len(linea) == 0:
        continue
    contador += 1
    # Enviar línea
    uart.write(linea + "\n")
    print("Enviando línea", contador)
    print(linea)
    # Esperar ACK
    ack_recibido = False
    tiempo_ack = time.ticks_ms()
    while True:
        if uart.any():
            respuesta = uart.readline()
            if respuesta:
                respuesta = respuesta.decode().strip()
                if respuesta == "ACK":
                    ack_recibido = True
                    print("ACK recibido")
                else:
                    print("Respuesta:", respuesta)
                break
        # Timeout
        if time.ticks_diff(
            time.ticks_ms(),
            tiempo_ack
        ) > 10000:
            print("ERROR: timeout esperando ACK")
            break
    # Si no se recibió ACK
    if not ack_recibido:
        print()
        print("TRANSFERENCIA INTERRUMPIDA")
        break
    # Intervalo entre líneas
    if intervalo > 0:
        time.sleep(intervalo)
# FINALIZACIÓN
archivo.close()
tiempo_fin = time.ticks_ms()
tiempo_total_ms = time.ticks_diff(
    tiempo_fin,
    tiempo_inicio
)
tiempo_total_s = tiempo_total_ms / 1000
# RESULTADOS
print()
print("       TRANSFERENCIA FINALIZADA")
print("Líneas enviadas:", contador)
print("Intervalo:", intervalo, "segundos")
print("Tiempo total:", tiempo_total_s, "segundos")
if contador > 0:
    promedio = tiempo_total_s / contador
    print(
        "Tiempo promedio por línea:",
        promedio,
        "segundos"
    )