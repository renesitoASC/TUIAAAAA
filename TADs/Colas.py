class Nodo1:
    def __init__(self,dato:any=None,prox:'Nodo1'| None=None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)
    

class cola:
    def __init__(self):
        self.items = []
    def insert(self,x:any):
        self.items.append(x)

    def remove(self):
        if self.isEmpty():
            print('La cola esta vacia.')         # IMPLEMENTACION DE COLAS CON LISTAS
            return
        return self.items.pop(0)
    
    def isEmpty(self):
        return len(self.items) == 0
    
class ColaConListasEnlazadas:
    def __init__(self):
        self.prim = None
        self.len = 0

    def isEmpty(self):
        return (self.len == 0)
    
    def insert(self,data:any):
        nodoAinsertar = Nodo1(data)
        if self.isEmpty():
            self.prim = nodoAinsertar
        else:
            NodoActual= self.prim
            while NodoActual.prox:
                NodoActual = NodoActual.prox
            NodoActual.prox = nodoAinsertar
        self.len += 1

    def remove(self):
        if self.isEmpty():
            print('Cola vacia.')
            return
        dato = self.prim.dato
        self.prim = self.prim.prox
        self.len -= 1
        return dato
    

class ColaMejorada:
    def __init__(self):
        self.len = 0
        self.prim = None
        self.ult = None
    
    def isEmpty(self):
        return (self.len == 0)
    
    def insert(self,data:any):
        nodoAinsertar = Nodo1(data)
        if self.isEmpty():
            self.prim=self.ult=nodoAinsertar
        else:
            UltimoNodo = self.ult
            UltimoNodo.prox = nodoAinsertar
            self.ult = nodoAinsertar
        self.len += 1

    def remove(self):
        if self.isEmpty():
            print('Cola vacia')
            return
        data = self.prim.dato
        self.prim = self.prim.prox
        self.len -= 1
        if self.len == 0:
            self.ult = None
        return data