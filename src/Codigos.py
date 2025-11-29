import os

def limpiar():
    try:
        os.system("cls")
    except:
        pass

usuarios_administrador = {
    "admin": "1234",}

precios = {"sencilla": 15,"doble": 20,"familia": 48,
           "turismo": 20,"alimentacion": 4,"mascotas": 15}

costos_resort = {
    "sencilla": {"general": 7, "extra": 10},
    "doble": {"general": 10, "extra": 15},
    "familia": {"general": 24, "extra": 35},
    "turismo": {"general": 10, "extra": 15},
    "alimentacion": {"general": 2, "extra": 3},
    "mascotas": {"general": 8, "extra": 8}
}

alistamiento = {"sencilla": 0,"doble": 0,"familia": 0,"turismo": 0,"alimentacion": 0}

lista_clientes = []

def validar_nombre(nombre):
    return nombre.isalpha() and len(nombre) >= 3

def validar_apellido(apellido):
    return apellido.isalpha() and len(apellido) >= 3

def validar_documento(documento):
    return documento.isdigit() and 3 <= len(documento) <= 15

def planear_alistamiento():
    limpiar()
    print("Alistamiento inicial del resort\n")
    try:
        alistamiento["sencilla"] = int(input("Cantidad de habitaciones sencillas disponibles: "))
        alistamiento["doble"] = int(input("Cantidad de habitaciones dobles disponibles: "))
        alistamiento["familia"] = int(input("Cantidad de habitaciones familiares disponibles: "))
        alistamiento["turismo"] = int(input("Cupos para turismo disponibles: "))
        alistamiento["alimentacion"] = int(input("Cupos para alimentación disponibles: "))
    except:
        print("\nDebe ingresar números válidos.")
        input("ENTER para continuar...")
        return

    print("\nAlistamiento registrado correctamente.")
    input("ENTER para continuar...")

def registrar_persona():
    while True:
        nombre = input("Nombre: ")
        if validar_nombre(nombre):
            break
        print("Nombre inválido.")

    while True:
        apellido = input("Apellido: ")
        if validar_apellido(apellido):
            break
        print("Apellido inválido.")

    while True:
        documento = input("Documento: ")
        if validar_documento(documento):
            break
        print("Documento inválido.")

    return {
        "nombre": nombre,
        "apellido": apellido,
        "documento": documento
    }

def registrar_cliente():
    limpiar()
    print("Registro de cliente\n")
    print("Tipos de grupo disponibles:")
    print("1. Individual")
    print("2. Pareja")
    print("3. Familia")

    tipo_opcion = input("Seleccione el tipo: ")

    if tipo_opcion == "1":
        tipo = "sencilla"
        cantidad_personas = 1
    elif tipo_opcion == "2":
        tipo = "doble"
        cantidad_personas = 2
    elif tipo_opcion == "3":
        tipo = "familia"
        cantidad_personas = 4
    else:
        print("Opción no válida.")
        input("ENTER para continuar...")
        return

    if alistamiento[tipo] > 0:
        tipo_servicio_base = "general"
        alistamiento[tipo] -= 1
    else:
        tipo_servicio_base = "extra"

    personas = []
    for _ in range(cantidad_personas):
        print("\nIngrese los datos de la persona:")
        personas.append(registrar_persona())

    print("\n¿Incluye servicio de turismo? (s/n)")
    respuesta_turismo = input("> ").lower()
    tiene_turismo = respuesta_turismo == "s"

    if tiene_turismo:
        if alistamiento["turismo"] > 0:
            tipo_turismo = "general"
            alistamiento["turismo"] -= 1
        else:
            tipo_turismo = "extra"
    else:
        tipo_turismo = None

    print("\n¿Incluye alimentación? (s/n)")
    respuesta_alimento = input("> ").lower()
    tiene_alimentacion = respuesta_alimento == "s"

    if tiene_alimentacion:
        if alistamiento["alimentacion"] > 0:
            tipo_alimentacion = "general"
            alistamiento["alimentacion"] -= 1
        else:
            tipo_alimentacion = "extra"
    else:
        tipo_alimentacion = None

    try:
        mascotas = int(input("\nCantidad de mascotas: "))
    except:
        mascotas = 0

    precio_base_cliente = precios[tipo]
    costo_base_resort = costos_resort[tipo][tipo_servicio_base]

    if tiene_turismo:
        precio_turismo_cliente = precios["turismo"]
        costo_turismo_resort = costos_resort["turismo"][tipo_turismo]
    else:
        precio_turismo_cliente = 0
        costo_turismo_resort = 0

    if tiene_alimentacion:
        precio_alimento_cliente = precios["alimentacion"]
        costo_alimento_resort = costos_resort["alimentacion"][tipo_alimentacion]
    else:
        precio_alimento_cliente = 0
        costo_alimento_resort = 0

    precio_mascotas_cliente = mascotas * precios["mascotas"]
    costo_mascotas_resort = mascotas * costos_resort["mascotas"]["general"]

    costo_total_cliente = precio_base_cliente + precio_turismo_cliente + precio_alimento_cliente + precio_mascotas_cliente
    costo_total_resort = costo_base_resort + costo_turismo_resort + costo_alimento_resort + costo_mascotas_resort

    cliente = {
        "tipo": tipo,
        "tipo_servicio_base": tipo_servicio_base,
        "personas": personas,
        "tiene_turismo": tiene_turismo,
        "tipo_turismo": tipo_turismo,
        "tiene_alimentacion": tiene_alimentacion,
        "tipo_alimentacion": tipo_alimentacion,
        "mascotas": mascotas,
        "costo_base_cliente": precio_base_cliente,
        "costo_base_resort": costo_base_resort,
        "costo_turismo_cliente": precio_turismo_cliente,
        "costo_turismo_resort": costo_turismo_resort,
        "costo_alimentacion_cliente": precio_alimento_cliente,
        "costo_alimentacion_resort": costo_alimento_resort,
        "costo_mascotas_cliente": precio_mascotas_cliente,
        "costo_mascotas_resort": costo_mascotas_resort,
        "costo_total_cliente": costo_total_cliente,
        "costo_total_resort": costo_total_resort
    }

    lista_clientes.append(cliente)

    print("\nCliente registrado correctamente.")
    input("ENTER para continuar...")

def admin():
    limpiar()
    print("Inicio de sesión administrador\n")
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if usuario not in usuarios_administrador or usuarios_administrador[usuario] != clave:
        print("\nAcceso denegado.")
        input("ENTER para continuar...")
        return

    while True:
        limpiar()
        print("====================================")
        print("        MÓDULO ADMINISTRADOR")
        print("====================================")
        print("1. Total de clientes en el hotel")
        print("2. Total por tipo de habitación")
        print("3. Total de mascotas")
        print("4. Disponibilidad de habitaciones")
        print("5. Disponibilidad de turismo y alimentación")
        print("6. Ventas")
        print("7. Costos")
        print("8. Ganancia")
        print("9. Ver detalles completos de los clientes")
        print("0. Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            total_personas = sum(len(c["personas"]) for c in lista_clientes)
            print("\nTotal de personas en el hotel:", total_personas)
            input("ENTER...")

        elif opcion == "2":
            conteo = {"sencilla": 0, "doble": 0, "familia": 0}
            for c in lista_clientes:
                conteo[c["tipo"]] += 1

            print("\nClientes por tipo de habitación:")
            for tipo, cant in conteo.items():
                print(f"{tipo}: {cant}")
            input("ENTER...")

        elif opcion == "3":
            mascotas = sum(c["mascotas"] for c in lista_clientes)
            print("\nTotal de mascotas:", mascotas)
            input("ENTER...")

        elif opcion == "4":
            print("\nDisponibilidad actual:\n")
            print("Sencilla:", alistamiento["sencilla"])
            print("Doble:", alistamiento["doble"])
            print("Familia:", alistamiento["familia"])
            input("ENTER...")

        elif opcion == "5":
            print("\nServicios disponibles:\n")
            print("Turismo:", alistamiento["turismo"])
            print("Alimentación:", alistamiento["alimentacion"])
            input("ENTER...")

        elif opcion == "6":
            ventas = sum(c["costo_total_cliente"] for c in lista_clientes)
            print("\nVentas totales:", ventas)
            input("ENTER...")

        elif opcion == "7":
            costos = sum(c["costo_total_resort"] for c in lista_clientes)
            print("\nCostos totales:", costos)
            input("ENTER...")

        elif opcion == "8":
            ventas = sum(c["costo_total_cliente"] for c in lista_clientes)
            costos = sum(c["costo_total_resort"] for c in lista_clientes)
            print("\nGanancia:", ventas - costos)
            input("ENTER...")

        elif opcion == "9":
            limpiar()
            print("Detalles completos de clientes:\n")

            if len(lista_clientes) == 0:
                print("No hay clientes registrados.")
                input("ENTER...")
                continue

            for c in lista_clientes:
                print("-------------------------------------")
                print("Tipo de habitación:", c["tipo"])
                print("Servicio base:", c["tipo_servicio_base"])

                print("\nPersonas registradas:")
                for persona in c["personas"]:
                    print(f"  - {persona['nombre']} {persona['apellido']}  |  Doc: {persona['documento']}")

                print("\nTurismo:", "Sí" if c["tiene_turismo"] else "No")
                if c["tiene_turismo"]:
                    print("  Tipo:", c["tipo_turismo"])

                print("Alimentación:", "Sí" if c["tiene_alimentacion"] else "No")
                if c["tiene_alimentacion"]:
                    print("  Tipo:", c["tipo_alimentacion"])

                print("Mascotas:", c["mascotas"])
                print("Costo total cliente:", c["costo_total_cliente"])
                print("Costo total resort:", c["costo_total_resort"])
                print("-------------------------------------\n")

            input("ENTER...")

def menu():
    while True:
        limpiar()
        print("====================================")
        print("            SIRUMA RESORT")
        print("     Sistema de Gestión del Hotel")
        print("====================================")
        print("1. Planeación del alistamiento")
        print("2. Registrar un cliente")
        print("3. Módulo administrador")
        print("0. Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            planear_alistamiento()
        elif opcion == "2":
            registrar_cliente()
        elif opcion == "3":
            admin()
        elif opcion == "0":
            print("\nSaliendo del sistema...")
            break
        else:
            print("Opción inválida.")
            input("ENTER...")

menu()

