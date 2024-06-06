class Greedy:
    def __init__(self, matrix):
        self.matrix = matrix

    def greedy_coloring(self):
        n = len(self.matrix)
        colors = [-1] * n
        color = 0

        # Fungsi untuk memeriksa apakah warna yang diberikan aman untuk digunakan pada node tertentu
        def is_safe(node, color):
            for i in range(n):
                if self.matrix[node][i] == 1 and colors[i] == color:
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
