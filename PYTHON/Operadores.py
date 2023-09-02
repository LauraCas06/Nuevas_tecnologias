#LOS OPERADORES LOGICOS CON PYTHON

#CONDICIONAL 1 = Python 

#age = 18
#height = 150

# igual e igual
#if  height == 100 and age == 10:
 #  print("El niño puede ingresar") 

#menor e igual
#if height <=100 and age <=10:
   #print("El niño no puede ingresar")

#mayor e igual
#if height >= 100 and age >=10:
 #   print("El niño puede ingresar porque cumple ambas caracteristicas")


#menor o igual
#if height <= 100 or age <=10:
 #  print("El niño no puede ingresar porque no cumple ninguna caracteristicas")

#mayor o igual 
#if height >= 100 or age >=10:
 #   print("El niño puede ingresar")


#CONDICIONAL 2 = Python

age = int(input("Ingrese su edad = "))
height = int(input("Ingrese su estatura = "))

if height > 150 and age >= 17: 
      print("Si  - Puede ingresar al Martillo")

else: 
     print("No cumple la edad y la altura requerida")