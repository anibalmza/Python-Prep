# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
variable = 12
print(variable)

# 2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(variable))

# 4) Crear una variable que contenga tu nombre
nombre = 'Anibal'

# 5) Crear una variable que contenga un número complejo
complejo = 5 + 7j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(complejo))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
import math 
pi = round(math.pi,4)
print(pi)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
vble_texto = 'True'
vble_bool = True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(vble_texto))
print(type(vble_bool))

# 10) Asignar a una variable, la suma de un número entero y otro decimal
variable2 = 15 + 10.25

# 11) Realizar una operación de suma de números complejos
suma_complejos = 5+3j + 10+2j

# 12) Realizar una operación de suma de un número real y otro complejo
suma = 10.25 + 8+3j
# 13) Realizar una operación de multiplicación
multi = 12 * 3

# 14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
division = 27/4
print(division)

# 16) De la división anterior solamente mostrar la parte entera
division = 27//4
print(division)

# 17) De la división de 27 entre 4 mostrar solamente el resto
resto = 27%4
print(resto)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
resultado = division * 4 + resto
print(resultado)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print('Hola'+' buen'+' día')

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
if("2" == 2):
    print("son iguales")
else:
    print("No son iguales")

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
if(int("2") == 2):
    print("son iguales")
else:
    print("No son iguales")

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# Porque lleva punto No coma

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
variable3 = 3
variable3-=1

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1 << 2)
# convierte el numero a binario y corre dos lugares a la izquierda
# 001 -> 100 = 4

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
suma2 = str(2) + '2'
print(suma2)

suma3 = 2 + int('2')
print(suma3)

# 26) Realizar una operación válida entre valores de tipo entero y string
palabra = 'Casa '
print(palabra * 3)