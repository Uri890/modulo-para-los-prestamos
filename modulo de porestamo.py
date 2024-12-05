# Clase para representar un Usuario
class Usuario:
    def __init__(self, nombre, edad, numero_cuenta):
        self.__nombre = nombre
        self.__edad = edad
        self.__numero_cuenta = numero_cuenta

    # Métodos para acceder y modificar los atributos (encapsulamiento)
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def set_numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    def __str__(self):
        return f"Usuario: {self.__nombre}, Edad: {self.__edad}, Cuenta: {self.__numero_cuenta}"


# Clase para representar un Libro
class Libro:
    def __init__(self, titulo, autor, editorial, categoria):
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria

    # Métodos para acceder y modificar los atributos (encapsulamiento)
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_editorial(self):
        return self.__editorial

    def get_categoria(self):
        return self.__categoria

    def __str__(self):
        return f"'{self.__titulo}' por {self.__autor} ({self.__editorial}) - Categoría: {self.__categoria}"


# Clase para representar una Categoría
class Categoria:
    def __init__(self, nombre):
        self.__nombre = nombre

    # Método para acceder al nombre
    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return f"Categoría: {self.__nombre}"


# Clase para gestionar la Biblioteca
class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []

    # Métodos para manejar libros y usuarios
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def agregar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.__libros if libro.get_titulo().lower() == titulo.lower()]
        return resultados

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.__libros if libro.get_autor().lower() == autor.lower()]
        return resultados

    def buscar_por_categoria(self, categoria):
        resultados = [libro for libro in self.__libros if libro.get_categoria().lower() == categoria.lower()]
        return resultados


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Agregar categorías
    categoria_ficcion = Categoria("Ficción")
    categoria_historia = Categoria("Historia")

    # Agregar libros
    libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "Editorial XYZ", categoria_ficcion.get_nombre())
    libro2 = Libro("Sapiens", "Yuval Noah Harari", "Editorial ABC", categoria_historia.get_nombre())
    libro3 = Libro("1984", "George Orwell", "Editorial DEF", categoria_ficcion.get_nombre())

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Agregar usuarios
    usuario1 = Usuario("María Moreno", 25, "U001")
    biblioteca.agregar_usuario(usuario1)

    # Buscar libros por título
    print("Búsqueda por título: 'El principito'")
    for libro in biblioteca.buscar_por_titulo("El principito"):
        print(libro)

    # Buscar libros por autor
    print("\nBúsqueda por autor: 'George Orwell'")
    for libro in biblioteca.buscar_por_autor("George Orwell"):
        print(libro)

    # Buscar libros por categoría
    print("\nBúsqueda por categoría: 'Ficción'")
    for libro in biblioteca.buscar_por_categoria("Ficción"):
        print(libro)
