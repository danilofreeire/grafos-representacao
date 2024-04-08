
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
    def __init__(self,from_=None,to_=None,weight=None,active=True):
        self.from_ = from_ # NÓ DE ORIGEM
        self.to_ = to_ # NÓ DE DESTINO
        self.weight = weight  #PESO
        self.active = active #SE O NÓ ESTÁ ATIVO
    
    def to_str(self):
        if self.weight is not None:
            return f"{'{'}{self.from_.tag},{self.to_.tag},{self.weight}{'}'}" #{ NOME NÓ ORIGEM , NOME NÓ DESTINO , PESO }
        else:
            return f"{'{'}{self.from_.tag},{self.to_.tag}{'}'}" #{ NOME NÓ ORIGEM , NOME NÓ DESTINO , PESO }

    
class Graph:

    def __init__(self,oriented=True):
        self.V = {} # DICIONARIO QUE ARMAZENA OS NÓS(VERTICES)
        self.E = {} # DICIONARIO QUE ARMAZENA AS ARESTAS
        self.oriented = oriented # DEFINE O GRÁFICO COMO ORIENTADO
       

    def print_me(self):
        for n in self.V: #PARA CADA NÓ N NO DICIONARIO V, OU SEJA, ITERA SOBRE OS NÓS DO GRAFO
            node = self.V[n] #OBTEMOS O OBJETO NÓ CORRESPONDENTE AO NOME DO NÓ ATUAL REPRESENTADO PELA TAG 'N' : N É A CHAVE E O NO É O VALOR ASSOCIADO.
            str_=''
            print(f"{node.tag} {node.neighbor_to_str()}") # IMPRIME AS INFORMAÇÕES SOBRE O NÓ ATUAL { NOME DO NÓ -> VIZINHOS ->VIZINHOS}
        for e in self.E: #ITERAS SOBRE AS ARESTAS DO GRAFO
            print(self.E[e].to_str()) #OBTEMOS O OBJETO COM A CHAVE 'e', OU SEJA, A ARESTA ATUAL E COLOCAMOS ELA EM REPRESENTAÇÃO DE STRING

    def add_node(self,tag): #RECEBE COMO PARAMETRO O NOME DO NÓ
        if tag in self.V: return#SE O NÓ ESTÁ NO DICIONARIO V, ELE PARA 
        node = Node(tag)# SE O NÓ NÃO ESTÁ ELE CRIA UM OBJETO NÓ COM O NOME  RECEBIDO
        self.V[tag] = node #ADICIONA O NÓ NO DICIONARIO V, A CHAVE = NOME E VALOR CORRESPONDENTE = NÓ
    
    def get_node(self,tag): #RECEBE O NOME DO NÓ
        if tag not in self.V: #SE O NÓ NÃO ESTÁ NO DICIONARIO V
            self.add_node(tag) #ADICIONA ESSE NÓ NO DICIONARIO V
        return self.V[tag] # SE O NÓ ESTÁ, APENAS RETORNA ELE 

    def add_edge(self,tag_from,tag_to,weight= None):#RECEBE O NÓ DE ORIGEM, NÓ DE DESTINO E PESO

        frm = self.get_node(tag_from) #PEGA O NÓ DE ORIGEM
        to = self.get_node(tag_to)#PEGA O NÓ DE DESTINO

        frm.add_neighbor(to) # ADICIONA O NÓ DE DESTINO COMO VIZINHO DO NÓ DE ORIGEM
        if not self.oriented: # SE O GRAFO NÃO É ORIENTADO
             to.add_neighbor(frm) #ADICIONA O NÓ DE ORIGEM COMO VIZINHO DO NÓ DE DESTINO

        if weight is not None: #CRIA UM OBJETO ARESTA COM PESO
            edge = Edge(frm, to, weight)
        else: #CRIA UM OBJETO ARESTA SEM PESO
            edge = Edge(frm, to)

        k1 = frm.tag+10000*to.tag #CRIA UMA CHAVE ESPECIFICA
        self.E[k1] = edge #ADICIONA O OBJETO ARESTA NO DICIONARIO E
        
# Criando um objeto Graph
graph = Graph()

# Adicionando nós ao grafo
graph.add_node("0")
graph.add_node("1")
graph.add_node("2")
graph.add_node("3")
graph.add_node("4")

# Adicionando arestas ao grafo SEM PESO
graph.add_edge("0", "3")
graph.add_edge("0", "2")
graph.add_edge("1", "3")
graph.add_edge("4", "1")
graph.add_edge("2", "4")
# Imprimindo informações sobre o grafo
graph.print_me()

# Criando um objeto Graph
graph = Graph()

# Adicionando nós ao grafo
graph.add_node("0")
graph.add_node("1")
graph.add_node("2")
graph.add_node("3")
graph.add_node("4")

# Adicionando arestas ao grafo COM PESO
graph.add_edge("0", "3", 3)
graph.add_edge("0", "2", 11)
graph.add_edge("1", "3", 42)
graph.add_edge("4", "1", 3)
graph.add_edge("2", "4", 7)
# Imprimindo informações sobre o grafo
graph.print_me()