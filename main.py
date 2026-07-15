
print("===================================")
print(" GENERADOR DE CÓDIGO DESTINO ")
print("===================================")

# Leer una línea de código
codigo = input("Escriba una línea de código: ")

# ---------- TRADUCCIÓN ----------
codigo = codigo.replace("print(", "console.log(")
codigo = codigo.replace("True", "true")
codigo = codigo.replace("False", "false")

# Agregar "let" a las variables
if "=" in codigo and "==" not in codigo:
    partes = codigo.split("=")

    if len(partes) == 2:
        variable = partes[0].strip()
        valor = partes[1].strip()

        codigo = f"let {variable} = {valor}"

# ---------- OPTIMIZACIÓN ----------
codigo = codigo.replace("0 + ", "")
codigo = codigo.replace("+ 0", "")
codigo = codigo.replace("1 * ", "")
codigo = codigo.replace("* 1", "")
codigo = codigo.replace("/ 1", "")
codigo = codigo.replace("- 0", "")

# ---------- CÓDIGO DESTINO ----------
nombre_archivo = "codigoDestino.js"

with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("// Código generado automáticamente\n")
    archivo.write(codigo)

print("\nCódigo destino generado correctamente.\n")
print(codigo)

print("\nArchivo creado:", nombre_archivo)