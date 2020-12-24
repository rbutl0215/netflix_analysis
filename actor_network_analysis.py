import networkx as nx
import matplotlib.pyplot as plt
import pandas
import json 
import operator 

def read_data():
    df = pandas.read_csv('working_relationships.csv')
    return df

def init_graph():
    G = nx.Graph()
    return G

def add_edges(G_,df_):
    size = len(df_.index)
    for i in range(0,size):
        G_.add_edge(df_.iloc[i,0],df_.iloc[i,1])
    return G_

def draw_graph(G_):
    pos = nx.spring_layout(G_,k=0.1,iterations=20)
    betCent = nx.betweenness_centrality(G_, normalized=True, endpoints=True)
    node_color = [20000.0 * G_.degree(v) for v in G_]
    node_size =  [v * 3000 for v in betCent.values()]
    nx.draw_networkx(G_, pos, with_labels=True, font_size=2, width = 0.1, node_color = node_color, node_size = node_size)
    plt.show()
    return

def eigenvector_centrality(G_):
    centrality = nx.eigenvector_centrality(G_)
    centrality = dict(sorted(centrality.items(), key=lambda item: item[1], reverse=True))
    json_object = json.dumps(centrality, indent=4)
    with open("eigenvector_centrality.json", "w") as outfile: 
        outfile.write(json_object) 
    return


def main():
    df = read_data()
    G = init_graph()
    G = add_edges(G,df)
    eigenvector_centrality(G)

if __name__ == '__main__':
    main()