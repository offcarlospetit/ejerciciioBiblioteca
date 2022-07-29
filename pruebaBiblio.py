class Biblioteca():
    def __init__(self,nombre_bi="",libros=[],nombre_lib=""):
        self.nombre_bi=nombre_bi
        self.libros=libros
        self.nombre_lib=nombre_lib

    

    def __str__(self):
        l= f"Libros: \n"
        for nombre_lib in self.libros:
            l+=f"{nombre_lib}\n"
        return l

    def anadirLibro(self):
        continuar=True
        while continuar:
            buscar_biblio=input("Ingrese nombre de biblioteca: ")
            for b in Contenedor(self.bibliotecas):
                if b.nombre_bi==buscar_biblio:
                    nombre=input("Ingrese nombre de libro: ")
                    lib=Libro(nombre)
                    self.libros.append(lib)
                    for l in self.libros:
                        if l.nombre_lib==nombre:
                            print(l)
                            respuesta=input("¿Desea agregar otro libro? (s/n)")
                            if respuesta != "s" and respuesta != "S":
                                continuar=False
                else:
                    print("Libro no encontrado en esta biblioteca")


    def buscarLibro(self):
        pass
        





class Libro():
    def __init__(self,nombre_lib=""):
        self.nombre_lib=nombre_lib

    
    def __str__(self):
       lib=self.nombre_lib
       return lib

    

class Contenedor(Biblioteca):
    OPC_ANADIR_BIBLIOTECA=1
    OPC_CONSULTAR_BIBLIOTECA=2
    OPC_ANADIR_LIBRO=3
    OPC_BUSCAR_LIBRO=4
    OPC_SALIR=5
    
    def __init__(self,nombre_bi="",bibliotecas=[]):
        super().__init__(nombre_bi)
        self.bibliotecas=bibliotecas

    def __str__(self):
        b= f"Bibliotecas: \n"
        for nombre_bi in self.bibliotecas:
            b+=f"{nombre_bi}\n"
        return b


    def menu(self):
        continuar=True
        while continuar:
            print (f'''
        {self.OPC_ANADIR_BIBLIOTECA} Añadir biblioteca
        {self.OPC_CONSULTAR_BIBLIOTECA} Consultar biblioteca
        {self.OPC_ANADIR_LIBRO} Añadir libro
        {self.OPC_BUSCAR_LIBRO} Buscar libro
        {self.OPC_SALIR} Salir
        ''')

            opc=int(input("Selecciona una opción: "))
            if opc==self.OPC_ANADIR_BIBLIOTECA:            
                self.anadirBiblio()
            elif opc==self.OPC_CONSULTAR_BIBLIOTECA:
                self.consultarBiblio()
            elif opc==self.OPC_ANADIR_LIBRO:
                Biblioteca.anadirLibro(self)
            elif opc==self.OPC_BUSCAR_LIBRO:
                self.buscarLibro()
            elif opc==self.OPC_SALIR:
                continuar=False
                print("Nos vemos")
                break


    def anadirBiblio(self):
        continuar=True
        while continuar:
            nombre_bi=input("Ingrese nombre de biblioteca: ")
            biblio=Biblioteca(nombre_bi)
            self.bibliotecas.append(biblio)
            respuesta=input("¿Desea agregar otra biblioteca? (s/n)")
            if respuesta != "s" and respuesta != "S":
                continuar=False
                

    def consultarBiblio(self):

        print("Bibliotecas")
        #si hay bibliotecas que las muestre
        if len(self.bibliotecas)==0:
            print("No hay bibliotecas registradas")
        else:
            #ciclo para mostrar
            for b in self.bibliotecas:
                print(f"{b}")

    


        

bi=Contenedor()
bi.menu()

        
