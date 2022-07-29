# Ingresar bibliotecas a una lista, y luego en cualquiera de esas bibliotecas, que se buscan por nombre, añadir libros.
# Guardar los libros en una lista, dentro de la biblioteca seleccionada, y despues tener la opción de consultarlos


# crear clase biblioteca con sus atributos


class Libro():
    libros = []

    def __init__(self, nombre_lib=""):
        if(nombre_lib != ""):
            self.setLibro(nombre_lib)

# Se añade libros
    def setLibro(self, nombre_lib):
        self.libros.append(nombre_lib)

    def getLibros(self):
        return self.libros

    def getLibro(self, nombre_lib):
        for libro in self.libros:
            if libro == nombre_lib:
                return libro
        return None

    def __str__(self):
        b = f"Libros: \n"
        for libro in self.libros:
            b += f"{libro}\n"
        return b


class Biblioteca():

    # inicializar
    def __init__(self, nombre_bi="", libros: Libro = []):
        self.nombre_bi = nombre_bi
        self.libros = libros

    # metodo str para imprimir
    def __str__(self):
        b = f"Biblioteca: \n" + f"{self.nombre_bi}\n"
        return b

    def setLibros(self, libros):
        self.libros = libros

    def getLibros(self):
        return self.libros

    def getName(self):
        return self.nombre_bi

    def setName(self, nombre_bi):
        self.nombre_bi = nombre_bi


bibliotecas = []


def main():
    continuar = True
    OPC_ANADIR_BIBLIOTECA = 1
    OPC_CONSULTAR_BIBLIOTECA = 2
    OPC_ANADIR_LIBRO = 3
    OPC_BUSCAR_LIBRO = 4
    OPC_SALIR = 5
    #  declare a list of Class biblioteca

    while continuar:
        print(f'''
            {OPC_ANADIR_BIBLIOTECA} Añadir biblioteca
            {OPC_CONSULTAR_BIBLIOTECA} Consultar biblioteca
            {OPC_ANADIR_LIBRO} Añadir libro
            {OPC_BUSCAR_LIBRO} Buscar libro
            {OPC_SALIR} Salir
            ''')
        opc = int(input("Selecciona una opción: "))
        if opc == OPC_ANADIR_BIBLIOTECA:
            añadeBiblioteca()
        elif opc == OPC_CONSULTAR_BIBLIOTECA:
            consultaBiblioteca()
        elif opc == OPC_ANADIR_LIBRO:
            añadirLibros()
        elif opc == OPC_BUSCAR_LIBRO:
            buscarLibro()
        elif opc == OPC_SALIR:
            continuar = False
            print("Nos vemos")
            break


def consultaBiblioteca():
    select = input(
        "Ingrese nombre de biblioteca a buscar: ")
    biblioteca: Biblioteca
    for biblioteca in bibliotecas:
        if(select == biblioteca.getName()):
            print("Heureka! Se ha encontrado la biblioteca: ",
                  biblioteca.getName())
            break
        else:
            print("No se ha encontrado la biblioteca: ", biblioteca.getName())
            break
    return


def buscarLibro():
    select = input(
        "Ingrese nombre de biblioteca donde buscar el libro: ")
    bibli: Biblioteca
    for bibli in bibliotecas:
        print(select, bibli.getName())
        if select == bibli.getName():
            selectedBiblio = bibli
            break
        else:
            print("No está ingresada esa biblioteca")
            break
    nombre_lib = input("Ingrese libro a consultar: ")
    libro: Libro
    if(selectedBiblio.libros.getLibro(nombre_lib) != None):
        print("el libro " + selectedBiblio.libros.getLibro(nombre_lib) +
              " se encuentra en la biblioteca " + selectedBiblio.getName())
    else:
        print("No se encontró el libro")
    return


def añadirLibros():
    libros = Libro()
    if len(bibliotecas) == 0:
        print("No hay bibliotecas registradas")
    else:
        continuar = True
        bibli: Biblioteca
        x = 0
        biblioFind = 0
        selectedBiblio: Biblioteca
        select = input(
            "Ingrese nombre de biblioteca donde ingresar libro: ")
        for bibli in bibliotecas:
            print(bibli.getName(), select)
            if select == bibli.getName():
                selectedBiblio = bibli
                biblioFind = x
                break
            else:
                print("No está ingresada esa biblioteca")
            x += 1
        while continuar:
            nombre_lib = input("Ingrese libro: ")
            libros.setLibro(nombre_lib)
            respuesta = input("¿Desea agregar otro libro? (s/n)")
            if respuesta != "s" and respuesta != "S":
                continuar = False
        selectedBiblio.setLibros(libros)
        bibliotecas[biblioFind] = selectedBiblio
    return


def añadeBiblioteca():
    continuar = True
    while continuar:
        nombre_bi = input("Ingrese nombre de biblioteca: ")
        biblioteca = Biblioteca(nombre_bi)
        bibliotecas.append(biblioteca)
        respuesta = input("¿Desea agregar otra biblioteca? (s/n)")
        if respuesta != "s" and respuesta != "S":
            continuar = False
    return


main()
