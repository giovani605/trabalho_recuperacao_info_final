import facebook
import matplotlib.pyplot as plt
import networkx as nx
import pprint
import pickle
# por padrao eh node 1 -> node 2
def ligar_nodes(node1,node2,grafo,cor):
    # add a aresta




    
    grafo.add_edge(node1,node2,edge_color='red')

limite = 3

def furacao(a, nodee,grafo):
    print("----------")
    print(nodee)
    print a
    if listaGlobal.has_key(nodee['name']):
        print nodee['name'] + "duplicado "
        return

    if a is limite:
        return
    listaGlobal2[nodee['name']] = nodee['name']

    lista = graph.get_connections(id=nodee['id'], connection_name='likes')
    for p in lista['data']:
        print("     " + p['name'])
        ligar_nodes(nodee['name'],p['name'],grafo,"blue")
        furacao(a=a + 1, nodee=p,grafo=grafo)
    print("----------")
    return;


def busca_feed(a, nodee,grafo,nome):
    print("----------")
    print(nome)
    print a
    if listaGlobal.has_key(nome):
        print nome + "duplicado "
        return
    if a is limite:
        return

    listaGlobal[nome] = nome
    listafeed = graph.get_connections(id=nodee['id'], connection_name='posts')
    lista = []
    for li  in  listafeed['data']:
        #print li

        if li.has_key('story'):
            try:
                origem = graph.get_connections(id=li['id'],connection_name='attachments')
#            print origem['data']['url']

                for o in origem['data']:
                    if o.has_key('target'):
                        algumacoisa = o['target']
                        #posso ser feliz
                        if algumacoisa.has_key('id'):
                                pagina = graph.get_object(id=algumacoisa['id'],fields='from')
                                print pagina
                                ligar_nodes(nodee['name'],pagina['from']['name'],grafo,"black")
                                lista.append(pagina['from'])
            except facebook.GraphAPIError:
                print "excessao"
                continue

    for x in lista:
        busca_feed(a + 1, x, grafo, x['name'])
    print("----------")
    return;








G = nx.DiGraph()
G2 = nx.DiGraph()
id = "316647148819555"
secret_app = "515d7ec4e21a3e8f845376b3d8a63412"
token = "EAACEdEose0cBAA4E2Gf79rscyyjU7LnNEna2lLL75uaL2UyWJWtCCy715QrNgn908QZAItP5RZCd9pmuuFl2tAkzFS3jFjhE3L4cwZBb4QobHRbVTYQLj9PaIKk0z6Fdv56xFOpboQLaK4SnsiUfZCC4EdkdfsXDYCpyhDugQGUly9PtGxnZBBgZCdPPMGRPsZD"
graph = facebook.GraphAPI(access_token=token, version="2.7")
post = graph.get_connections(id='903483879742143', connection_name='likes')
print("comecando")
listaGlobal = {}
listaGlobal2 = {}
for node in post['data']:
    furacao(0,node,G2)
for node in post['data']:
    busca_feed(0, node,G,node['name'])

pickle.dump(G,open('grafo_post_pronto_3.pkl', 'wb'))

pickle.dump(G2,open('grafo_furacao_pronto_3.pkl', 'wb'))