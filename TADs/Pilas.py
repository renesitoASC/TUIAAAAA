class Nodo1:
    def __init__(self,dato:any=None,prox:'Nodo1'| None=None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)
    
class Pila:
    def __init__(self):
        self.items = [] # SIEMPRE SE INICIALIZA VACIA, SIN NINGUN ATRIBUTO QUE PASARLE.

    def push(self,data:any):
        self.items.append(data)

    def isEmpty(self):
        return (self.items == [])
    
    def pop(self):
        if self.isEmpty():
            print('La pila esta vacia.')
            return
        return self.items.pop()
    

class PilasConListasEnlazadas:
    def __init__(self):
        self.len = 0
        self.prim = None

    def IsEmpty(self):
        return (self.len == 0)
    
    def push(self,data:any):
        nuevoNodo = Nodo1(data)
        nuevoNodo.prox = self.prim
        self.prim = nuevoNodo
        self.len += 1
    def pop(self):
        if self.IsEmpty():
            print('Pila vacia.')
            return
        data = self.prim.dato
        self.prim = self.prim.prox
        self.len -= 1
        return data