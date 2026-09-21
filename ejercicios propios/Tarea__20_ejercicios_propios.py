# TAREA 1 - 20 EJERCICIOS POR CUENTA PROPIA
# Tema: Clases y Colecciones en Python

# EJERCICIO 1 - Números positivos
class NumerosPositivos:
    def __init__(self):
        self.numeros = []

    def agregar(self, numero):
        if numero > 0:
            self.numeros.append(numero)

    def agregar_varios(self, *numeros):
        for numero in numeros:
            self.agregar(numero)


objeto1 = NumerosPositivos()
objeto1.agregar_varios(5, -2, 8, 0, 10)
print("Ejercicio 1:", objeto1.numeros)


# EJERCICIO 2 - Registro de nombres
class RegistroNombres:
    def __init__(self):
        self.nombres = []

    def agregar(self, nombre):
        self.nombres.append(nombre)

    def mostrar(self):
        return self.nombres

    def cantidad(self):
        return len(self.nombres)


objeto2 = RegistroNombres()
objeto2.agregar("Ana")
objeto2.agregar("Luis")
objeto2.agregar("Pedro")

print("Ejercicio 2:", objeto2.mostrar())
print("Cantidad de nombres:", objeto2.cantidad())


# EJERCICIO 3 - Control de asistencia
class Asistencia:
    def __init__(self):
        self.estudiantes = {}

    def registrar(self, nombre, presente):
        self.estudiantes[nombre] = presente

    def mostrar_presentes(self):
        presentes = []

        for nombre in self.estudiantes:
            if self.estudiantes[nombre] == True:
                presentes.append(nombre)

        return presentes


objeto3 = Asistencia()
objeto3.registrar("Maria", True)
objeto3.registrar("Juan", False)
objeto3.registrar("Carlos", True)

print("Ejercicio 3:", objeto3.mostrar_presentes())


# EJERCICIO 4 - Productos baratos
class Productos:
    def __init__(self):
        self.productos = {}

    def agregar(self, nombre, precio):
        self.productos[nombre] = precio

    def buscar_baratos(self, limite):
        baratos = []

        for nombre in self.productos:
            if self.productos[nombre] <= limite:
                baratos.append(nombre)

        return baratos


objeto4 = Productos()
objeto4.agregar("Cuaderno", 2.50)
objeto4.agregar("Mochila", 25)
objeto4.agregar("Lapiz", 1)

print("Ejercicio 4:", objeto4.buscar_baratos(5))


# EJERCICIO 5 - Múltiplos de 3
class MultiplosDeTres:
    def __init__(self):
        self.multiplos = []
        self.no_multiplos = []

    def revisar(self, numero):
        if numero % 3 == 0:
            self.multiplos.append(numero)
        else:
            self.no_multiplos.append(numero)

    def revisar_varios(self, *numeros):
        for numero in numeros:
            self.revisar(numero)


objeto5 = MultiplosDeTres()
objeto5.revisar_varios(3, 5, 6, 8, 9, 10)

print("Ejercicio 5 - Múltiplos:", objeto5.multiplos)
print("Ejercicio 5 - No múltiplos:", objeto5.no_multiplos)


# EJERCICIO 6 - Calculadora de precios
class Calculadora:
    def __init__(self):
        self.precios = []

    def agregar(self, precio):
        self.precios.append(precio)

    def calcular_total(self):
        return sum(self.precios)

    def aplicar_descuento(self, porcentaje):
        total = self.calcular_total()
        descuento = total * porcentaje / 100
        return total - descuento


objeto6 = Calculadora()
objeto6.agregar(10)
objeto6.agregar(20)
objeto6.agregar(30)

print("Ejercicio 6 - Total:", objeto6.calcular_total())
print("Con 10% de descuento:", objeto6.aplicar_descuento(10))


# EJERCICIO 7 - Agenda telefónica
class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def buscar(self, nombre):
        if nombre in self.contactos:
            return self.contactos[nombre]
        else:
            return "No existe el contacto"


objeto7 = Agenda()
objeto7.agregar("Sofia", "099111222")
objeto7.agregar("Daniel", "098333444")

print("Ejercicio 7:", objeto7.buscar("Sofia"))


# EJERCICIO 8 - Clasificador de palabras
class Palabras:
    def __init__(self):
        self.cortas = []
        self.largas = []

    def clasificar(self, palabra):
        if len(palabra) <= 4:
            self.cortas.append(palabra)
        else:
            self.largas.append(palabra)

    def agregar_varias(self, *palabras):
        for palabra in palabras:
            self.clasificar(palabra)


objeto8 = Palabras()
objeto8.agregar_varias("sol", "computadora", "casa", "programacion")

print("Ejercicio 8 - Cortas:", objeto8.cortas)
print("Ejercicio 8 - Largas:", objeto8.largas)


# EJERCICIO 9 - Control de edades
class Edades:
    def __init__(self):
        self.edades = []

    def agregar(self, edad):
        self.edades.append(edad)

    def mayores_de_edad(self):
        mayores = []

        for edad in self.edades:
            if edad >= 18:
                mayores.append(edad)

        return mayores


objeto9 = Edades()
objeto9.agregar(15)
objeto9.agregar(20)
objeto9.agregar(17)
objeto9.agregar(25)

print("Ejercicio 9:", objeto9.mayores_de_edad())


# EJERCICIO 10 - Registro de ciudades
class Ciudades:
    def __init__(self):
        self.ciudades = set()

    def agregar(self, ciudad):
        self.ciudades.add(ciudad)

    def agregar_varias(self, *ciudades):
        for ciudad in ciudades:
            self.agregar(ciudad)


objeto10 = Ciudades()
objeto10.agregar_varias("Quito", "Guayaquil", "Cuenca", "Quito")

print("Ejercicio 10:", objeto10.ciudades)


# EJERCICIO 11 - Calificaciones
class Calificaciones:
    def __init__(self):
        self.notas = []

    def agregar(self, nota):
        self.notas.append(nota)

    def notas_aprobadas(self):
        aprobadas = []

        for nota in self.notas:
            if nota >= 70:
                aprobadas.append(nota)

        return aprobadas


objeto11 = Calificaciones()
objeto11.agregar(80)
objeto11.agregar(55)
objeto11.agregar(90)
objeto11.agregar(65)

print("Ejercicio 11:", objeto11.notas_aprobadas())


# EJERCICIO 12 - Inventario de libros
class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar(self, nombre, cantidad):
        self.libros[nombre] = cantidad

    def mostrar_disponibles(self):
        disponibles = []

        for libro in self.libros:
            if self.libros[libro] > 0:
                disponibles.append(libro)

        return disponibles

    def prestar(self, libro):
        if libro in self.libros and self.libros[libro] > 0:
            self.libros[libro] = self.libros[libro] - 1
            return True
        else:
            return False


objeto12 = Biblioteca()
objeto12.agregar("Python basico", 3)
objeto12.agregar("Matematicas", 0)

print("Ejercicio 12:", objeto12.mostrar_disponibles())
print("Se pudo prestar:", objeto12.prestar("Python basico"))


# EJERCICIO 13 - Contador de letras
class ContadorLetras:
    def __init__(self):
        self.letras = {}

    def contar(self, texto):
        self.letras = {}

        for letra in texto.lower():
            if letra.isalpha():
                if letra in self.letras:
                    self.letras[letra] = self.letras[letra] + 1
                else:
                    self.letras[letra] = 1

        return self.letras


objeto13 = ContadorLetras()
print("Ejercicio 13:", objeto13.contar("banana"))


# EJERCICIO 14 - Lista de compras
class ListaCompras:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def eliminar(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def mostrar(self):
        return self.productos


objeto14 = ListaCompras()
objeto14.agregar("Pan")
objeto14.agregar("Leche")
objeto14.agregar("Huevos")
objeto14.eliminar("Leche")

print("Ejercicio 14:", objeto14.mostrar())


# EJERCICIO 15 - Promedio de números pares
class NumerosPares:
    def __init__(self):
        self.pares = []

    def agregar(self, numero):
        if numero % 2 == 0:
            self.pares.append(numero)

    def agregar_varios(self, *numeros):
        for numero in numeros:
            self.agregar(numero)

    def promedio(self):
        if len(self.pares) == 0:
            return 0

        return sum(self.pares) / len(self.pares)


objeto15 = NumerosPares()
objeto15.agregar_varios(2, 4, 5, 8, 10)

print("Ejercicio 15:", objeto15.pares)
print("Promedio:", objeto15.promedio())


# EJERCICIO 16 - Conversor de temperatura
class Temperatura:
    def __init__(self):
        self.resultados = []

    def convertir(self, celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        self.resultados.append(fahrenheit)
        return fahrenheit

    def convertir_varias(self, *temperaturas):
        for temperatura in temperaturas:
            self.convertir(temperatura)

        return self.resultados


objeto16 = Temperatura()
print("Ejercicio 16:", objeto16.convertir_varias(0, 20, 30))


# EJERCICIO 17 - Registro de mascotas
class Mascotas:
    def __init__(self):
        self.mascotas = {}

    def agregar(self, nombre, tipo):
        self.mascotas[nombre] = tipo

    def buscar_perros(self):
        perros = []

        for nombre in self.mascotas:
            if self.mascotas[nombre] == "perro":
                perros.append(nombre)

        return perros


objeto17 = Mascotas()
objeto17.agregar("Firulais", "perro")
objeto17.agregar("Michi", "gato")
objeto17.agregar("Luna", "perro")

print("Ejercicio 17:", objeto17.buscar_perros())


# EJERCICIO 18 - Operaciones con conjuntos
class Conjuntos:
    def unir(self, conjunto1, conjunto2):
        return conjunto1.union(conjunto2)

    def elementos_comunes(self, conjunto1, conjunto2):
        return conjunto1.intersection(conjunto2)


objeto18 = Conjuntos()

a = {1, 2, 3}
b = {3, 4, 5}

print("Ejercicio 18 - Unión:", objeto18.unir(a, b))
print("Ejercicio 18 - Comunes:", objeto18.elementos_comunes(a, b))


# EJERCICIO 19 - Registro de películas
class Peliculas:
    def __init__(self):
        self.peliculas = []

    def agregar(self, nombre, nota):
        self.peliculas.append((nombre, nota))

    def mostrar_buenas(self):
        buenas = []

        for pelicula in self.peliculas:
            if pelicula[1] >= 8:
                buenas.append(pelicula)

        return buenas

    def promedio(self):
        total = 0

        for pelicula in self.peliculas:
            total = total + pelicula[1]

        if len(self.peliculas) == 0:
            return 0

        return total / len(self.peliculas)


objeto19 = Peliculas()
objeto19.agregar("Pelicula A", 8.5)
objeto19.agregar("Pelicula B", 6.5)
objeto19.agregar("Pelicula C", 9)

print("Ejercicio 19:", objeto19.mostrar_buenas())
print("Promedio:", objeto19.promedio())


# EJERCICIO 20 - Analizador de números
class Analizador:
    def __init__(self):
        self.numeros = []

    def agregar(self, numero):
        self.numeros.append(numero)

    def agregar_varios(self, *numeros):
        for numero in numeros:
            self.agregar(numero)

    def mayor(self):
        return max(self.numeros)

    def menor(self):
        return min(self.numeros)

    def suma(self):
        return sum(self.numeros)


objeto20 = Analizador()
objeto20.agregar_varios(12, 5, 20, 8, 15)

print("Ejercicio 20 - Mayor:", objeto20.mayor())
print("Ejercicio 20 - Menor:", objeto20.menor())
print("Ejercicio 20 - Suma:", objeto20.suma())
