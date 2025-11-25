class BinaryTree:
    def _init_(self,cargo:any):
        self.cargo = cargo
        self.left = None
        self.right = None

    def _str_(self):
        return str(self.cargo) 
    
class BinaryTree2:
    def _init_(self):
        self.raiz = None        # OTRA FORMA DE DEFINIR ARBOLES, DONDE DEFINIMOS LA RAIZ COMO NONE