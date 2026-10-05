

def entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numer valido")

class Libro:
    def __init__(self,titulo,autor,disponible):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible




class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self,titulo,autor):
        objeto = Libro(titulo,autor,True)
        self.libros.append(objeto)
   
    
    def prestar_libro(self,titulo):
        if not self.libros:
            print("En este momento la bibliblioteca esta vacia")
        else:
            for libro in self.libros:
                if libro.titulo.lower() == titulo:
                    if libro.disponible:
                        libro.disponible = False
                        print("El libro esta disponible\n...\nPrestando libro")
                        return
                    else:
                        print("El libro existe pero ya esta prestado")
                        return
            print("El libro no existe en la biblioteca")
    
    def devolver_libro(self,titulo):
        if not self.libros:
            print("En este momento la bibliblioteca esta vacia")
        else:
            for libro in self.libros:
                if libro.titulo.lower() == titulo:
                    if not libro.disponible:
                        libro.disponible = True
                        print("Gracias por la devolver el libro")
                        return
                    else:
                        print("No se ha prestado el libro")
                        return
            print("Ese libro no pertenece a esta biblioteca")
        
                    
               
        
        
def main():
    biblioteca = Biblioteca()
    while True:
        opcion =entero("======================\n  Welcome biblioteca\n======================\n1)Agregar libro\n2)Prestar libro\n3)Devolver libro\n4)Salir\nIngrese opcion:")
        if opcion == 1:
            ingre_titulo = input("Ingrese el titulo del libro: ").lower()
            autor = input("Ingrese el nombre del autor del libro: ").lower()
            biblioteca.agregar_libro(ingre_titulo,autor)
        elif opcion == 2:
            prestar_titulo = input("¿Que libro buscas?\n").lower()
            biblioteca.prestar_libro(prestar_titulo)
        elif opcion == 3:
            devolver_titulo = input("Ingrese el nombre del libro que desea devolver: ").lower()
            biblioteca.devolver_libro(devolver_titulo)
        elif opcion == 4:
            break
        else:
            print("Ingrese opcion valida")

main()
    