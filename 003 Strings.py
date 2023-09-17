mensaje = "Hola"
mensaje += " "
mensaje += "Andres"
print(mensaje)

print("Concatenacion:")

mensaje = "Hola"
espacio = " "
nombre = "Andres"
print(mensaje + espacio + nombre)

numero_uno = 4
numero_dos = 5
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es:" + resultado)

print("Busqueda:")

mensaje = "Hola Andres"
buscar_subcadena = mensaje.find("Andres")
print(buscar_subcadena)

print("Comparacion:")

mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)

print("Busqueda:")

mensaje = "Hola Andres"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)
