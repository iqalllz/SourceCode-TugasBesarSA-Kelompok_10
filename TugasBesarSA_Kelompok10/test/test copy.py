activities = []


def greedy_coloring(matrix):
    n = len(matrix)
    colors = [-1] * n
    color = 0

    # Fungsi untuk memeriksa apakah warna yang diberikan aman untuk digunakan pada node tertentu
    def is_safe(node, color):
        for i in range(n):
            if matrix[node][i] == 1 and colors[i] == color:
                return False
        return True

    # Pewarnaan greedy
    for node in range(n):
        # Coba warnai node dengan warna yang belum digunakan pada tetangganya
        for c in range(color):
            if is_safe(node, c):
                colors[node] = c
                break
        # Jika tidak ada warna yang aman, gunakan warna baru
        if colors[node] == -1:
            colors[node] = color
            color += 1

    return colors


def generate_colored_graph(matrix):
    G = nx.from_numpy_array(matrix)
    pos = nx.spring_layout(G)  # Layout untuk menempatkan node secara visual

    colors = greedy_coloring(matrix)

    nx.draw_networkx_nodes(
        G, pos, node_size=700, node_color=colors, cmap=plt.cm.rainbow
    )  # Gambar node dengan warna
    nx.draw_networkx_labels(G, pos)  # Label node

    # Gambar edges
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                nx.draw_networkx_edges(
                    G, pos, edgelist=[(i, j)], width=2, alpha=0.5, edge_color="b"
                )

    plt.axis("off")  # Hilangkan sumbu x dan y
    plt.show()


def display_activities():
    print("Daftar Kegiatan:")
    for i, activity in enumerate(activities):
        print(f"{i+1}. {activity}")


def add_activity(new_activity):
    activities.append(new_activity)


import os
import numpy as np


def convert_to_numerical():
    numerical_activities = {activity: i for i, activity in enumerate(activities)}
    return numerical_activities


def generate_input_matrix(numerical_activities):
    n = len(numerical_activities)
    matrix = np.zeros((n, n), dtype=int)

    # Contoh hardcoded hubungan antar kegiatan
    matrix[0][1] = 1  # Kegiatan 1 dihubungkan dengan kegiatan 2
    matrix[1][0] = 1  # Kegiatan 2 dihubungkan dengan kegiatan 3
    matrix[2][0] = 1  # Kegiatan 3 dihubungkan kembali dengan kegiatan 1
    matrix[0][2] = 1  # Kegiatan 1 juga dihubungkan dengan kegiatan 3

    matrix[2][4] = 1
    matrix[4][2] = 1

    matrix[4][3] = 1
    matrix[3][4] = 1

    matrix[3][1] = 1
    matrix[1][3] = 1

    return matrix


import networkx as nx
import matplotlib.pyplot as plt


def generate_graph(adj_matrix):
    rows = len(adj_matrix)
    cols = rows

    G = nx.from_numpy_array(adj_matrix)
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
        (i, j): adj_matrix[i][j]
        for i in range(rows)
        for j in range(cols)
        if adj_matrix[i][j] != 0
    }

    node_labels = {i: chr(i + 65) for i in range(len(adj_matrix))}

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)

    plt.show()


add_activity("Membuat Laporan")
add_activity("Presentasi Kegiatan")
add_activity("Melakukan Revisi")
add_activity("Meeting")
add_activity("Wawancara")
display_activities()

numerical_activities = convert_to_numerical()
print("Konversi ke numerical:", numerical_activities)

input_matrix = generate_input_matrix(numerical_activities)
print("Matriks Input:")
print(input_matrix)

generate_colored_graph(input_matrix)
