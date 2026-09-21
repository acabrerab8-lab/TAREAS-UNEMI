# TAREA 1 - 20 EJERCICIOS CON APOYO DE IA
# Tema: Clases y Colecciones en Python
# Nota: Código elaborado a partir de la guía de ejercicios proporcionada.

# ============================================================
# EJERCICIO 1 - Validador de notas con promedio
# ============================================================
class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)


c = Calificador()
print("1.", c.cargar_notas(85, 92, 110, 78, -5, 88))
print("Promedio:", c.promedio())


# ============================================================
# EJERCICIO 2 - Contador de palabras únicas
# ============================================================
class AnalizadorTexto:
    def __init__(self):
        self.palabras = []
        self.unicas = set()

    def agregar_palabra(self, palabra):
        self.palabras.append(palabra)
        self.unicas.add(palabra)

    def contar_palabras(self):
        return len(self.unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)
        return self.palabras


at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola", "python")
print("2.", at.palabras)
print("Palabras únicas:", at.contar_palabras())


# ============================================================
# EJERCICIO 3 - Gestor de compras con totales
# ============================================================
class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        return [
            nombre for nombre, precio in self.articulos.items()
            if precio_min <= precio <= precio_max
        ]


cc = CarroCompras()
cc.agregar_articulo("pan", 2.50)
cc.agregar_articulo("leche", 3.00)
cc.agregar_articulo("arroz", 5.00)
print("3. Total:", cc.total_carrito())
print("Artículos entre 2 y 4:", cc.articulos_por_rango(2, 4))


# ============================================================
# EJERCICIO 4 - Inversor de secuencias
# ============================================================
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            original = tuple(lista)
            resultado[original] = self.invertir_lista(lista)
        return resultado


inv = InversorSecuencia()
print("4.", inv.invertir_lista([1, 2, 3]))
print("Múltiples:", inv.invertir_multiples([1, 2, 3], [4, 5]))


# ============================================================
# EJERCICIO 5 - Detector de números pares e impares
# ============================================================
class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        self.pares = []
        self.impares = []

        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)

        return {"pares": self.pares, "impares": self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))


an = AnalizadorNumeros()
print("5.", an.separar(1, 2, 3, 4, 5))
print("Cantidades:", an.cantidad_pares_impares())


# ============================================================
# EJERCICIO 6 - Estadísticas de temperatura
# ============================================================
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)
        return self.temperaturas


gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print("6.", gt.temperaturas)
print("Mínima:", gt.minima())
print("Máxima:", gt.maxima())
print("Promedio:", gt.promedio())


# ============================================================
# EJERCICIO 7 - Mapeador de edades
# ============================================================
class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        return [
            nombre for nombre, edad in self.personas.items()
            if edad >= edad_minima
        ]

    def edad_promedio(self):
        if not self.personas:
            return 0
        return sum(self.personas.values()) / len(self.personas)


gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
gp.agregar_persona("Carlos", 35)
print("7.", gp.personas_mayores(18))
print("Edad promedio:", gp.edad_promedio())


# ============================================================
# EJERCICIO 8 - Asignador de equipos
# ============================================================
class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        return max(self.equipos, key=lambda equipo: len(self.equipos[equipo]))


eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.agregar_jugador("B", "Luis")
print("8.", eq.equipos)
print("Equipo con más integrantes:", eq.equipo_mayor_integrantes())


# ============================================================
# EJERCICIO 9 - Validador de caracteres
# ============================================================
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        vocales = 0
        consonantes = 0
        digitos = 0

        for caracter in texto:
            if caracter.isdigit():
                digitos += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    vocales += 1
                else:
                    consonantes += 1

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "digitos": digitos
        }


astr = AnalizadorString()
print("9.", astr.contar_por_tipo("Hola123"))
print("Texto más largo:", astr.texto_mas_largo)


# ============================================================
# EJERCICIO 10 - Gestor de tareas con prioridad
# ============================================================
class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [
            tarea for tarea in self.tareas
            if tarea[1].lower() == "alta"
        ]

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True
        return False


t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print("10.", t.tareas_prioritarias())
t.eliminar_completada("Leer")
print("Tareas restantes:", t.tareas)


# ============================================================
# EJERCICIO 11 - Contador de frecuencia
# ============================================================
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        if not self.frecuencias:
            return None
        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
cf.agregar_elemento("a")
print("11.", cf.frecuencias)
print("Más frecuente:", cf.elemento_mas_frecuente())
print("Frecuencia de a:", cf.frecuencia_elemento("a"))


# ============================================================
# EJERCICIO 12 - Selector de rango con tuplas
# ============================================================
class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()

        for inicio, fin in rangos:
            elementos.update(self.crear_rango(inicio, fin))

        return sorted(elementos)


sr = SelectorRango()
print("12.", sr.crear_rango(1, 3))
print("Elementos unicos:", sr.elementos_en_multiples_rangos((1, 3), (2, 4)))


# ============================================================
# EJERCICIO 13 - Combinador de listas
# ============================================================
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        mayor = max(len(lista1), len(lista2))

        for i in range(mayor):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []

        resultado = []
        maximo = max(len(lista) for lista in listas)

        for i in range(maximo):
            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])

        return resultado


cl = CombinadorListas()
print("13.", cl.intercalar([1, 2], [3, 4]))
print("Varias listas:", cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))


# ============================================================
# EJERCICIO 14 - Mapeo de estudiantes a notas
# ============================================================
class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        return [
            estudiante for estudiante, nota in self.notas.items()
            if nota >= nota_minima
        ]

    def mejor_estudiante(self):
        if not self.notas:
            return None
        nombre = max(self.notas, key=self.notas.get)
        return (nombre, self.notas[nombre])


rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 88)
print("14.", rn.estudiantes_aprobados(70))
print("Mejor estudiante:", rn.mejor_estudiante())


# ============================================================
# EJERCICIO 15 - Divisores de un numero
# ============================================================
class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = sum(divisor for divisor in divisores if divisor != numero)
        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


df = DivisorFinder()
print("15.", df.encontrar_divisores(12))
print("¿6 es perfecto?:", df.es_perfecto(6))
print("Múltiples:", df.encontrar_multiples_divisores(6, 10, 12))


# ============================================================
# EJERCICIO 16 - Codificador/Decodificador César
# ============================================================
class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra

        base = ord('a') if letra.islower() else ord('A')
        posicion = ord(letra) - base
        nueva_posicion = (posicion + desplazamiento) % 26

        return chr(base + nueva_posicion)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado
        return resultado


ccesar = CodificadorCesar()
print("16.", ccesar.codificar_palabra("hola", 3))
print("Historial:", ccesar.historial)


# ============================================================
# EJERCICIO 17 - Grupo de edades
# ============================================================
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])

        if not edades:
            return 0

        return sum(edades) / len(edades)


ae = AgrupadorEdades()
print("17.", ae.agrupar_por_categoria(5, 15, 30, 70))
print("Promedio de adultos:", ae.edad_promedio_categoria("adulto"))


# ============================================================
# EJERCICIO 18 - Matriz de distancias
# ============================================================
import math

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        distancia = math.sqrt(
            (p2[0] - p1[0]) ** 2 +
            (p2[1] - p1[1]) ** 2
        )
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None

        punto_cercano = puntos[0]
        distancia_menor = self.distancia_euclidiana(referencia, puntos[0])

        for punto in puntos[1:]:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano


cd = CalculadorDistancia()
print("18.", cd.distancia_euclidiana((0, 0), (3, 4)))
print("Punto mas cercano:", cd.punto_mas_cercano((0, 0), (5, 5), (1, 1), (3, 4)))


# ============================================================
# EJERCICIO 19 - Inventario de productos
# ============================================================
class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto not in self.stock:
            return False

        if self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True

        return False

    def productos_bajo_stock(self, minimo):
        return [
            producto for producto, cantidad in self.stock.items()
            if cantidad < minimo
        ]


inv = Inventario()
inv.agregar_stock("pan", 50)
inv.restar_stock("pan", 30)
print("19.", inv.stock)
print("¿Se puede restar 10?:", inv.restar_stock("pan", 10))
print("Productos bajo stock:", inv.productos_bajo_stock(15))


# ============================================================
# EJERCICIO 20 - Analizador de patrones en textos
# ============================================================
class AnalizadorPatrones:
    def __init__(self):
        self.texto = ""
        self.palabras = set()

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        return [
            palabra for palabra in palabras
            if palabra.lower().startswith(patron.lower())
        ]

    def agrupar_por_longitud(self, texto):
        resultado = {}

        for palabra in texto.split():
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        self.texto = texto
        return resultado

    def palabras_unicas(self):
        self.palabras = set(self.texto.split())
        return self.palabras


ap = AnalizadorPatrones()
texto = "el gato esta aqui y el gato juega"
print("20.", ap.encontrar_palabras(texto, "ga"))
print("Agrupadas:", ap.agrupar_por_longitud(texto))
print("Palabras unicas:", ap.palabras_unicas())
