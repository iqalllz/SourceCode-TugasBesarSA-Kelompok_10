class Backtracking:
    def __init__(self, matrix):
        self.matrix = matrix
        self.colors = []

    def is_safe(self, node, color):
        for i in range(len(self.matrix)):
            if self.matrix[node][i] == 1 and self.colors[i] == color:
                return False
        return True

    def backtracking_coloring(self, node):
        if node == len(self.matrix):
            return True
        for color in range(max(self.colors) + 2):
            if self.is_safe(node, color):
                self.colors[node] = color
                if self.backtracking_coloring(node + 1):
                    return True
                self.colors[node] = -1
        return False

    def color_graph(self):
        self.colors = [-1] * len(self.matrix)
        if not self.backtracking_coloring(0):
            return "No solution exists"
        return self.colors
