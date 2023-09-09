

prestamo = []
registro = []
login_correcto = False

def formulario():
    print("\n PRESTAMO: ")
    nombre = input("Ingrese su nombre: ")
    origen = input("Ingrese su origen: ")
    destino = input("Ingrese su destino: ")
    tarjeta = input("Ingrese numero de tarjeta")
    prestamo.append({"nombre": nombre, "origen": origen, "destino": destino, "tarjeta": tarjeta})
    print("Su codigo es:", tarjeta)

def registro():
    print("\nREGISTRO DE USUARIO:")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    tarjeta = int(input("Ingrese su codigo de prestamo: "))
    correo = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de teléfono: ")
    registro.append({"nombre": nombre, "apellido": apellido, "tarjeta": tarjeta, "correo": correo, "telefono": telefono})

def login():
    print("\nLOGIN DE USUARIO:")
    global login_exitoso
    nombre = input("Ingrese su nombre: ")
    for registro in registro:
        if registro["nombre"] == nombre:
            login_exitoso = True
            menu()
            return
    print("No encontrado")

def menu():
    print("MENU CONSULTAS:")
    opcion = int(input("Elija una opción:\n1. Consultas\n2. Préstamos\n"))
    if opcion == 1:
        informacion()
    elif opcion == 2:
        prestamos()

def informacion():
    nombre = input("Ingrese nombre: ")
    for registro in registro:
        if registro["nombre"] == nombre:
            print("Nombre:", registro["nombre"])
            print("Apellido:", registro["apellido"])
            print("Codigo prestamo:", registro["tarjeta"])
            print("Correo electrónico:", registro["correo"])
            print("Teléfono:", registro["telefono"])
            return
    print("No encontrado")

def prestamos():
    nombre = input("Ingrese su nombre: ")
    for prestamo in prestamos:
        if prestamo["nombre"] == nombre:
            print(" INFO PRESTAMO:")
            print("Número de tarjeta:", prestamo["tarjeta"])
            print("Origen:", prestamo["origen"])
            print("Destino:", prestamo["destino"])
            return
    print("Nombre no encontrado")

formulario()
registro()
login()
if login_exitoso:
    menu()