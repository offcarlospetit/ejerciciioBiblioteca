


class Contenedor:
    OPC_ANADIR_BIBLIOTECA=1
    OPC_CONSULTAR_BIBLIOTECA=2
    OPC_ANADIR_LIBRO=3
    OPC_BUSCAR_LIBRO=4
    OPC_SALIR=5
    
    def __init__(self):
        
        self.bibliotecas=[]
        self.nombre_bi=""

    def __str__(self):
        b= f"Bibliotecas: \n"
        for nombre_bi in self.bibliotecas:
            b+=f"{nombre_bi}\n"
        return b

    def setBiblio(self,nuevaBiblio):
        self.nombre_bi=nuevaBiblio

    def getBiblio(self):
        return self.nombre_bi

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
                self.anadirLibro()
            elif opc==self.OPC_BUSCAR_LIBRO:
                self.buscarLibro()
            elif opc==self.OPC_SALIR:
                continuar=False
                print("Nos vemos")
                break

    def anadirBiblio(self:
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

    def anadirLibro(self):
        
        continuar=True
        while continuar:
            for bib in self.bibliotecas:
                
                select=input("Ingrese nombre de biblioteca donde ingresar libro: ")
                if select == bib.nombre_bi:
                    nombre_lib=input("Ingrese libro: ")
                    libro=Libro(nombre_lib)
                    bib.libros.append(libro)
                else:
                    print("No está ingresada esa biblioteca")
                    
            respuesta=input("¿Desea agregar otro libro? (s/n)")
                

        
        




class Biblioteca:
    def __init__(self,nombre_bi=""):
        self.nombre_bi=nombre_bi
        self.libros=[]

    def __str__(self):
        return f"{self.nombre_bi}"
        l= f"Libros: \n"
        for biblio in self.bibliotecas:
            l+=f"{nombre_lib}\n"
        return l

    def setNombre_bi(self,nuevoNombre_bi):
        self.nombre_bi=nuevoNombre_bi        
        

    def getNombre_bi(self):
        return self.nombre_bi

    def setNombre_lib(self,nuevoNombre_lib):
        self.nombre_lib=nuevoNombre_lib

    def getNombre_lib(self):
        return self.nombre_lib

              
    
    


class Libro:
    def __init__(self,nombre_lib=""):
        self.nombre_lib=nombre_lib

    def setNombre_lib(self,nuevoNombre_lib):
        self.nombre_lib=nuevoNombre_lib
    
    def getNombre_lib(self):
        return self.nombre_lib

nuevo=Contenedor()
nuevo.menu()

    
    
