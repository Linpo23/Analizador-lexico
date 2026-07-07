codigo = []
variables = []

print("===== TRADUCTOR CON OPTIMIZADOR =====")

while True:

    linea = input()

    if linea.upper() == "FIN":
        break

    linea = linea.strip()

    if linea == "":
        continue

    # Traducción
    linea = linea.replace("print(", "console.log(")
    linea = linea.replace("True", "true")
    linea = linea.replace("False", "false")

    if "=" in linea and "let" not in linea:

        partes = linea.split("=")

        variable = partes[0].strip()
        valor = partes[1].strip()

        if variable not in variables:
            variables.append(variable)
            linea = f"let {variable} = {valor}"
        else:
            linea = f"{variable} = {valor}"

    # Optimización
    linea = linea.replace("0 + ", "")
    linea = linea.replace("+ 0", "")
    linea = linea.replace("- 0", "")
    linea = linea.replace("* 1", "")
    linea = linea.replace("1 * ", "")
    linea = linea.replace("/ 1", "")

    while "  " in linea:
        linea = linea.replace("  ", " ")

    codigo.append(linea)

print("\n===== CÓDIGO OPTIMIZADO =====")

for linea in codigo:
    print(linea)