print('Hola mundo')      # Texto entre comillas → imprime tal cual
print(7 + 4)             # Números → suma aritmética → 11
print('7' + '4')         # Cadenas → concatenación → '74'
print('Edad:', 25)       # Con comas puedes mezclar tipos → "Edad: 25"

nombre = 'Gustavo'       # Variable 'nombre' recibe una cadena
print('Hola,', nombre)   # Mezcla texto y variable con comas

x = input('Escribe algo: ')  # Siempre devuelve str
# Para sumar, convierte:
a = int(input('Dame un entero: '))
b = int(input('Otro entero: '))
print('Suma:', a + b)
