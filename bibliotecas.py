global listaBi
listaBi=list()

global listaLib
listaLib=list()




class Libro:
    def __init__(self):
        self.nombre_lib=""
        self.autor=""

#setters
    def setLibro(self,nuevoLibro):
        self.nombre_lib=nuevoLibro
        
    def setAutor(self,nuevoAutor):
        self.autor=nuevoAutor

#getters
    def getLibro(self):
        return self.nombre_lib

    def getAutor(self):
        return self.autor

#str
    def __str__(self):
        nombreLib=self.nombre_lib

class Biblioteca:
    def __init__(self, nombre_bi):
        self.nombre_bi=nombre_bi
        self.libro=None


#setters

    def setBiblio(self,nuevaBiblio):
        self.nombre_bi=nuevaBiblio

#Getters
        
    def getBiblio(self):
        return self.nombre_bi

#str
    def __str__(self):
        return self.nombre_bi
        

#funciones


def agregarBiblio():
    continuar=True
    while continuar:
        nombre_bi=input("Ingresar nombre de biblioteca: ")
        Mi_biblio_1 = Biblioteca(nombre_bi)
        listaBi.append(nombre_bi)
        #aca deberia imprimir la lista
        print(listaBi)


def menu():
    print("Elija una opcion: ")
    print("1.- Agregar biblioteca: ")
    print("2.- Agregar libro: ")
    print("3.- Consultar: ")
    seleccion=int(input("Elija una opcion: "))

    if seleccion==1:


        
        agregarBiblio()



menu()


