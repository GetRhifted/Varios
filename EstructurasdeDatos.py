# Creando una lista:
# fruits = []
# print(fruits)
# fruits.append('Manzana')
# print(fruits)
# fruits.append('Naranja')
# print(fruits)
# fruits.append('Limón')
# print(fruits)
# fruits.append('Banano')
# print(fruits)
# fruits.append('Fresa')
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.insert(0, 'Uva')
# print(fruits)
# fruits.insert(1, 'Melon')
# print(fruits)

#Ejemplo de funciones recursivas
def piramid_sum(lower, upper, margin=0):
    blanks = '' * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + piramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result
    
piramid_sum(1,4)