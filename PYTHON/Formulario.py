nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su numero de cedula: ")
edad = input("Cual es su edad :")
mascotas = input("tienes Mascotas? :")
isOn = bool(input("Seleccione 1 si es casado = "))

print("Su nombre es: " +nombre)
print("Su cedula es: " +cedula)
print("Su edad es: " +edad) 
print("Mascotas " +mascotas)

print( "Nombre = " + nombre + " / cedula = " +  cedula + " / Edad = " + edad)

print(type(isOn))
print(isOn)