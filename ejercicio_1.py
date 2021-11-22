# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

if numero_1 > numero_2 :
    print('El numero 1:' , numero_1, 'es mayor al numero 2:', numero_2 )
else :
    print('El numero 2:', numero_2, 'es mayor al numero 1:', numero_1)

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

if numero_1 > 0:
    print('El numero 1:', numero_1, 'es positivo')
elif numero_1 ==0:
    print('El numero 1:', numero_1, 'es igual a 0')
else :
    print('El numero 1:', numero_1, 'es negativo')


# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

if  100 > numero_1 > 0:
    print('El numero 1:', numero_1, 'cumple la condicion')
else:
    print('El numero 1:', numero_1, 'no cumple la condicion')

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condició

if numero_1<10 or numero_2>-2:
    print('La condicion se cumple')
else: 
    print('La condicion no se cumple')
