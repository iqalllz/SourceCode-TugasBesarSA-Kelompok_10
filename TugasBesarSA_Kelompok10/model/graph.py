import os
import networkx as nx
import matplotlib.pyplot as plt
from model.greedy import Greedy
from model.backtracking import Backtracking


class Graph:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def generate_colored_graph(self, method):
        G = nx.from_numpy_array(self.matrix)
        pos = nx.spring_layout(G)  # Layout untuk menempatkan node secara visual

        if method.lower() == "greedy":
            greedy = Greedy(self.matrix)
            colors = greedy.greedy_coloring()
        else:
            bt = Backtracking(self.matrix)
            colors = bt.color_graph()

        nx.draw_networkx_nodes(
            G, pos, node_size=700, node_color=colors, cmap=plt.cm.rainbow
        )  # Gambar node dengan warna
        node_labels = {i: chr(i + 65) for i in range(len(self.matrix))}
        nx.draw_networkx_labels(
            G,
            pos,
            labels=node_labels,
            font_size=8,
        )

        # Gambar edges
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] != 0:
                    nx.draw_networkx_edges(
                        G, pos, edgelist=[(i, j)], width=2, alpha=0.5, edge_color="gray"
                    )

        if not os.path.exists("static"):
            os.makedirs("static")

        if method.lower() == "greedy":
            plt.savefig("static/colored_graph_greedy.png")
        else:
            plt.savefig("static/colored_graph_backtracking.png")

        plt.box("off")
        plt.close()

    def generate_graph(self):
        rows = len(self.matrix)
        cols = rows

        G = nx.from_numpy_array(self.matrix)
        pos = nx.spring_layout(G)  # Layout graf

        plt.figure(figsize=(8, 6))
        nx.draw(
            G,
            pos,
            node_color="skyblue",
            node_size=2000,
            edge_color="gray",
        )

        # Tambahkan label tepi
        edge_labels = {
            (i, j): self.matrix[i][j]
            for i in range(rows)
            for j in range(cols)
            if self.matrix[i][j] != 0
        }

        node_labels = {i: chr(i + 65) for i in range(len(self.matrix))}

        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)

        if not os.path.exists("static"):
            os.makedirs("static")
        plt.savefig("static/graph.png")
        plt.close()
