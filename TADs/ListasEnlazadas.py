class Nodo1:
    def __init__(self,dato:any=None,prox:'Nodo1'| None=None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)

primerNodo = Nodo1(1)
segundoNodo = Nodo1(2,primerNodo)
tercerNodo = Nodo1(3,segundoNodo)

class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.len = 0
    
    def insert(self,data:any,index:int) -> None:
        if index > self.len or index < 0:
            print('Posicion invalida.')
            return
        nodo = Nodo1(data)

        if index==0:
            nodo.prox = self.prim 
            self.prim = nodo
        else:
            nodoAnterior = self.prim # SIEMPRE se utiliza este mismo atributo para 'situarnos' en la lista enlazada
            for pos in range(1,index):
                nodoAnterior = nodoAnterior.prox  # Va re-asignando el nodo anterior al que queremos insertar
            nodo.prox = nodoAnterior.prox # -------> IMPORTANTE <------ SIEMPRE se asigna el enlace del nuevo nodo
            nodoAnterior.prox = nodo # Y luego se rompe y se redirige el enlace (se asigna el nuevo nodo)
        self.len += 1

    def pop(self,index: int | None=None):
        if index is None:
            index = self.len - 1
        if index < 0 or index >= self.len:
            print('posicion invalida')
            return
        if index == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            nodoAnterior = self.prim # SIEMPRE se utilizan estos mismos dos atributos para 'situarnos' en la lista enlazada
            nodoActual = nodoAnterior.prox # SIEMPRE se utilizan estos mismos dos atributos para 'situarnos' en la lista enlazada
            for pos in range(1,index):
                nodoAnterior = nodoActual
                nodoActual = nodoAnterior.prox
            dato = nodoActual.dato
            nodoAnterior.prox = nodoActual.prox # ACA lo que hace es descartar el nodo, asignandole al nodo anterior del borrado su NUEVO enlace hacia el nodo proximo del nodo BORRADO. 
        self.len -= 1
        return dato
    
    def remove(self,datoBorrar: any) -> None:
        if self.len == 0:
            print('Lista vacia.')
            return
        if self.prim.dato == datoBorrar:
            self.prim = self.prim.prox
        else:
            nodoAnterior = self.prim  # SIEMPRE se utilizan estos mismos dos atributos para 'situarnos' en la lista enlazada
            nodoactual = nodoAnterior.prox # SIEMPRE se utilizan estos mismos dos atributos para 'situarnos' en la lista enlazada
            while nodoactual is not None and nodoactual.dato != datoBorrar:
                nodoAnterior = nodoactual
                nodoactual = nodoAnterior.prox  
                if nodoactual == None: # ACA es cuando compara con los datos de todos los nodos y NO encuentra coincidencia. (nodoAnterior.prox = None PORQUE ES EL ULTIMO NODO.)
                    print('Valor no encontrado en la lista.')
                    return
            # DESCARTAMOS el nodo
            nodoAnterior.prox = nodoactual.prox
            self.len -= 1


class Nodo2:
    def __init__(self,dato:any,prox:'Nodo2' | None=None,ante:'Nodo2'|None=None):
        self.dato = dato
        self.prox = prox
        self.ante = ante

        
class ListaDoblementeEnlazada:
    def __init__(self):
        self.len = 0 
        self.prim = None
        self.ultimo = None

    def isEmpty(self):
        return self.len == 0
    
    def insert(self,data:any,index:int) -> None:
        NuevoNodo = Nodo2(data)
        if index < 0 or index > self.len:
            print('Posicion invalida.')
            return
        if index == 0:
            if self.isEmpty():
                self.prim=self.anterior=NuevoNodo
            else:
                NuevoNodo.prox = self.prim
                self.prim.ante = NuevoNodo
                self.prim = NuevoNodo
        elif index == self.len:
            NuevoNodo.ante = self.ultimo
            self.ultimo.prox = NuevoNodo
            self.ultimo = NuevoNodo
        else:
            NodoAnterior = self.prim
            for pos in range(1,index):
                NodoAnterior = NodoAnterior.prox
            NuevoNodo.prox = NodoAnterior.prox
            NodoAnterior.prox.ante = NuevoNodo
            NodoAnterior.prox = NuevoNodo
            NuevoNodo.ante = NodoAnterior
        self.len += 1
    
    def pop(self,index:int|None=None) -> any:
        if self.isEmpty():
            print('La lista esta vacia.')
            return
        if index < 0 or index >= self.len:
            print('Posicion invalida.')
            return
            
        if index == None:     # si NO se pasa ningun atributo se elimina el ULTIMO nodo ingresado (self.ultimo)
            nodoAborrar = self.ultimo
            dato = nodoAborrar.dato
            if self.len == 1: # CASO donde solo existe 1 nodo en la lista doble
                self.prim=self.ultimo=None
            else: # si hay MAS de 1 nodo contenido.
                self.ultimo = nodoAborrar.ante
                self.ultimo.prox = None
        
        if index == 0:   # si se quiere eliminar el PRIMER nodo
            dato = self.prim.dato
            self.prim = self.prim.prox
        else: # Para cualquier indice
            NodoActual = self.prim
            for pos in range(1,index):
                NodoActual = NodoActual.prox
            dato = NodoActual.dato
            NodoAnterior = NodoActual.ante
            NodoSiguiente = NodoActual.prox

            



    
        
