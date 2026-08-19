print("       GENERADOR DE ALFABETOS")
# Alfabeto inglés
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    try:
        cantidad = int(input("¿Cuántas líneas desea generar? (1-1000): "))
        if 1 <= cantidad <= 1000:
            break
        print("ERROR: debe ingresar un número entre 1 y 1000.")
    except ValueError:
        print("ERROR: debe ingresar un número entero.")
# Crear archivo
with open("alfabetos.txt", "w") as archivo:
    for numero in range(1, cantidad + 1):
        linea = "{:04d} {}\n".format(numero, alfabeto)
        archivo.write(linea)
print()
print("Archivo alfabetos.txt creado correctamente.")
print("Número de líneas:", cantidad)
print()