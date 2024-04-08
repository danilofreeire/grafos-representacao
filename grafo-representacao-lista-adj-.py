
class Node:
    def __init__(self,tag=None):
        self.tag = tag  # NOME DO NÓ
        self.adj = []  # VIZINHOS DO NÓ
        self.color = 0 # COR DO NÓ
    def neighbor_to_str(self):
        s = "" 
        for n in self.adj:  # PERCORRE A LISTA DOS VIZINHOS DO NÓ 'N'
            s= s + f"->{n.tag}"  # PARA CADA NÓ 'N' ELE ADICIONA O NOME DO NÓ   
        return s
    def add_neighbor(self,node):
        self.adj.append(node) # ADICIONA O NÓ 'NODE' A LISTA 'SELF.ADJ'
        
class Edge:
    def __init__(self,from_=None,to=None,weight=None,active=True):
        self.from_ = from_ # NÓ DE ORIGEM
        self.to_ = to_ # NÓ DE DESTINO
        self.weight = weight  #PESO
        self.active = active #SE O NÓ ESTÁ ATIVO
    def to_str(self):
        return f"{'{'}{self.from_.tag},{self.to_.tag},{self.weight}{'}'}" #{ NOME NÓ ORIGEM , NOME NÓ DESTINO , PESO }
    