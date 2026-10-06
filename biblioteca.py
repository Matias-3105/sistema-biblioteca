import json

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
    
    def guardar(self):
        datos = []
        for libro in self.libros:
            datos.append({
                "titulo": libro.titulo,
                "autor": libro.autor,
                "disponible": libro.disponible,
            })
        with open("libros.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    
    def cargar(self):
        try:
            with open('libros.json','r') as archivo:
                        datos = json.load(archivo)
            for libro in datos:
                self.libros.append(Libro(libro["titulo"],libro["autor"],libro["disponible"]))     
        except FileNotFoundError:
            pass
    
    def agregar_libro(self,title,author):
        objeto = Libro(title,author,True)
        self.libros.append(objeto)
   
    
    def prestar_libro(self,titulo):
        if not self.libros:
            print("En este momento la bibliblioteca esta vacia")
        else:
            for libro in self.libros:
                if libro.titulo.lower() == titulo.lower():
                    if libro.disponible == True:
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
                if libro.titulo.lower() == titulo.lower():
                    if libro.disponible == False:
                        libro.disponible = True
                        print("Gracias por la devolver el libro")
                        return
                    else:
                        print("No se ha prestado el libro")
                        return
            print("Ese libro no pertenece a esta biblioteca")
        
                    
               
        
        
def main():
    biblioteca = Biblioteca()
    biblioteca.cargar()
    while True:
        opcion =entero("======================\n  Welcome biblioteca\n======================\n1)Agregar libro\n2)Prestar libro\n3)Devolver libro\n4)Salir\nIngrese opcion:")
        if opcion == 1:
            ingre_titulo = input("Ingrese el titulo del libro: ").lower()
            autor = input("Ingrese el nombre del autor del libro: ").lower()
            biblioteca.agregar_libro(ingre_titulo,autor)
            biblioteca.guardar()
        elif opcion == 2:
            prestar_titulo = input("¿Que libro buscas?\n").lower()
            biblioteca.prestar_libro(prestar_titulo)
            biblioteca.guardar()
        elif opcion == 3:
            devolver_titulo = input("Ingrese el nombre del libro que desea devolver: ").lower()
            biblioteca.devolver_libro(devolver_titulo)
            biblioteca.guardar()
        elif opcion == 4:
            
            break
        else:
            print("Ingrese opcion valida")

main()
    
