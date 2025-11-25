class Nodo3:
    def _init_(self,dato:any,izq:None,der:None):
        self.dato = dato
        self.izq = izq
        self.der = der

class Grafo:
    def _init_(self):
        self.vertices = [ ]
        self.relaciones = { }
    def add_node(self,x:any):
        if x not in self.vertices:
            self.vertices.append(x)
            self.relaciones[x] = [ ]

    def remove_node(self,x:any):
            if x in self.vertices:
                 self.vertices.remove(x)
                 for vec in self.relaciones[x]:
                      self.relaciones[vec].remove(x)
                 del self.relaciones[x]
    def add_relacion (self,x:any,y:any):
        self.add_node(x)
        self.add_node(y)
        if y not in self.relaciones[x]:
             self.relaciones[x].append(y)
        if x not in self.relaciones[y]:
             self.relaciones[y].append(x)

    def remove_relacion(self,x:any,y:any):
         if self.is_node(x) and self.is_node(y):
              if self.are_adyacent(x,y):
                self.relaciones[x].remove(y)
                self.relaciones[y].remove(x)
    

# METODOS A IMPLEMENTAR: is_node(),are_adyacent() y algunos mas...