# Ingresar bibliotecas a una lista, y luego en cualquiera de esas bibliotecas, que se buscan por nombre, añadir libros.
#Guardar los libros en una lista, dentro de la biblioteca seleccionada, y despues tener la opción de consultarlos



#crear clase biblioteca con sus atributos
class Biblioteca():

    #inicializar
    def __init__(self,bibliotecas=[],nombre_bi="",libros=[],nombre_lib=""):
        self.bibliotecas=[]
        self.nombre_bi=nombre_bi
        self.libros=libros
        self.nombre_lib=nombre_lib

    
    #metodo str para imprimir
    def __str__(self): 
        b= f"Bibliotecas: \n"
        for nombre_bi in self.bibliotecas:
            b+=f"{nombre_bi}\n"
        return b

    #no se si esto esta correcto, que haya 2 return en un str
        l= f"Libros: \n"
        for nombre_lib in self.libros:
            l+=f"{nombre_lib}\n"
        return l

    #metodo para añadir biblioteca

    def anadirBiblio(self):
        continuar=True
        while continuar:
            nombre_bi=input("Ingrese nombre de biblioteca: ")
            biblio=Biblioteca(nombre_bi)
            self.bibliotecas.append(biblio)            
            respuesta=input("¿Desea agregar otra biblioteca? (s/n)")
            if respuesta != "s" and respuesta != "S":
                continuar=False
                

    #metodo para consultar las bibliotecas ingresadas a la lista
    def consultarBiblio(self):

        print("Bibliotecas")
        #si hay bibliotecas que las muestre
        if len(self.bibliotecas)==0:
            print("No hay bibliotecas registradas")
        else:
            #ciclo para mostrar, no funciona.
            #El error puede estar en el str, en el guardado de la biblio en la lista o acá
            #los intente cambiar todos y nada me resulto
            for b in self.bibliotecas:
                print(f"{b}")

    #metodo para añadir libro

    def anadirLibro(self): 
        if len(self.bibliotecas)==0:
            print("No hay bibliotecas registradas") 
        else:
            continuar=True
            while continuar:                
                for bib in self.bibliotecas:                    
                    select=input("Ingrese nombre de biblioteca donde ingresar libro: ")
                    if select == bib.nombre_bib:
                        nombre_lib=input("Ingrese libro: ")
                        libro=Libro(nombre_lib)
                        self.libros.append(libro)
                    else:
                        print("No está ingresada esa biblioteca")
                        
                respuesta=input("¿Desea agregar otro libro? (s/n)")
                if respuesta != "s" and respuesta != "S":
                    continuar=False
                
            #for bib in self.bibliotecas:
             #   select=input("Ingrese nombre de biblioteca donde ingresar libro: ")
              #  if select == bib.nombre_bi:
               #     nombre_lib=input("Ingrese libro: ")
                #    libro=Libro(nombre_lib)
                 #   bib.libros.append(libro)
                #else:
                #    print("No está ingresada esa biblioteca")
                    
                    
        #continuar=True
       # while continuar:
            #busca la biblioteca en la cual ingresar el libro
          #  buscar_biblio=input("Ingrese nombre de biblioteca: ")
            #recorre la lista
           # for b in self.bibliotecas:
                #si encuentra el nombre, pide ingresar libro (no se si esto está bien)
              #  if b.nombre_bi==buscar_biblio:
               #     nombre=input("Ingrese nombre de libro: ")
               #     lib=Libro(nombre)
               #     self.libros.append(lib)
               #     for l in self.libros:
                #        if l.nombre_lib==nombre:
               #             print(l)
               #             respuesta=input("¿Desea agregar otro libro? (s/n)")
                #            if respuesta != "s" and respuesta != "S":
               #                 continuar=False
               # else:
               #1     print("Biblioteca no encontrada")


    def buscarLibro(self):
        pass
        





class Libro():
    def __init__(self,nombre_lib=""):
        self.nombre_lib=nombre_lib

    
    def __str__(self):
       lib=self.nombre_lib
       return lib

    
#acá va el menu
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
                Biblioteca.anadirBiblio(self)
            elif opc==self.OPC_CONSULTAR_BIBLIOTECA:
                Biblioteca.consultarBiblio(self)
            elif opc==self.OPC_ANADIR_LIBRO:
                Biblioteca.anadirLibro(self)
            elif opc==self.OPC_BUSCAR_LIBRO:
                Biblioteca.buscarLibro(self)
            elif opc==self.OPC_SALIR:
                continuar=False
                print("Nos vemos")
                break


    
bi=Contenedor()
bi.menu()

        
