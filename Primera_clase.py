#Función print
'''
print("Hola mundo")
print('Hola mundo 2')
'''

#Reasignacion de variable
'''
nombre = "Jose"
print(nombre)

nombre = "Carlos"
print(nombre)
'''

#Declarar varias variables
'''
a = b = c = 10
print(a)
print(b)
print(c)
'''

#Uso de funcion input
'''
nombre = input("Digita tu nombre: ")
apellido = input('Digita tu apellido: ')

print(nombre)
print(apellido)
'''

#Linea de blancos

#print("Hola como estas?\nEstoy muy bien")
#print("""Hola como estas?
#Estoy muy bien c:""")
#print('''Hola que tal.
#Estoy muy bien''')

#Anidaciones con print
'''
nombre = input("Cual es tu nombre? ")
apellido = input("Cual es tu apellido? ")

print("Hola mi nombre es "+nombre+" y mi apellido es "+apellido)
print("Hola mi nombre es {} y mi apellido es {}".format(nombre,apellido))
'''
#primer string
'''
primer_string = "Hola esto es un string"
segundo_string = 'Hola esto tambien es un string'

print(primer_string)
print(segundo_string)
'''

'''
string = "mario fuentes"
string_mayusculas = string.upper()
print(string)
print(string_mayusculas)

nombre = input("Digita tu  nombre completo: ")
print(nombre.title())

string = input("Digita un palabra: ")
print(string.lower())

frase = input("digita una frase: ")
contador = frase.count("mundo")
print(frase)
print(contador)

frase2 = input("Digita lo que gustes: ")
index = frase2.find("a")
print(frase2)
print(index)
'''

#IF ELSE
'''
edad = int(input("Cuantos años tienes? "))

if edad >= 18:
    print("Tienes {}, eres mayor de edad".format(edad))
else:
    print("Tienes {}, eres menor de edad".format(edad))
'''

#Nacionalidad
'''
nacionalidad = input("De que nacionalidad eres? ")

if nacionalidad.title() == "Mexicana":
    print("Eres mexicano")

elif  nacionalidad.title() == "Colombiana":
    print("Eres colombiano")
elif nacionalidad.title() == "Española":
    print("Eres español")
else:  
    print("Error al digitar")
'''

#Impuestos
'''
compra = float(input("Digita cual fue el gasto que hiciste: "))

if compra >= 100:
    total = compra * 1.16
else:
    total = compra

print("El total fue de ",round(total))
'''

#Suma, resta, multiplicacion
#primera opcion
'''
n1 = float(input("Digita el primer valor: "))
n2 = float(input("Digita el segundo valor: "))

opcion = int(input("""Digita que opcion deseas realizar: 
        1) suma
        2) resta
        3) multiplicacion
        :"""))

if opcion == 1:
    suma = n1 + n2
    print("La suma es igual a: ", suma)

elif opcion == 2:
    resta = n1 - n2
    print("La resta es igual a: ", resta)

elif opcion == 3:
    multiplicacion = n1*n2
    print("La multiplicacion es igual a: ", multiplicacion)

else:
    print("Opcion equivocada")
    '''
 #segunda opcion   

n1 = float(input("Digita el primer valor: "))
n2 = float(input("Digita el segundo valor: "))

opcion = int(input("""Digita que opcion deseas realizar: 
        1) suma
        2) resta
        3) multiplicacion
        :"""))

if opcion == 1:
    print("La suma es igual a: ", n1+n2)

elif opcion == 2:

    print("La resta es igual a: ", n1-n2)

elif opcion == 3:

    print("La multiplicacion es igual a: ", n1*n2)

else:
    print("Opcion equivocada")
    








