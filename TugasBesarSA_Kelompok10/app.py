import matplotlib

import model.graph

matplotlib.use("Agg")
import time
import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, send_file
import model

INF = float("inf")

app = Flask(__name__)


@app.route("/")
def index():
    if request.method == "POST":
        activities_count = request.form.get("activities_count", default=2, type=int)
    else:
        activities_count = 2  # Default value
    return render_template("index.html", activities_count=activities_count)


@app.route("/generate_graph", methods=["POST"])
def generate_graph():
    try:
        rows = int(request.form.get("activities_count", default=2, type=int))
        cols = rows

        matrix = []
        for i in range(rows):
            row = [int(request.form[f"matrix_{i}_{j}"]) for j in range(cols)]
            matrix.append(row)

        adj_matrix = np.array(matrix)

        graph = model.graph.Graph(adj_matrix)
        graph.generate_graph()

        st_gr = time.perf_counter()
        graph.generate_colored_graph("Greedy")
        ct_gr = time.perf_counter()
        et_gr = round(ct_gr - st_gr, 5)

        st_bt = time.perf_counter()
        graph.generate_colored_graph("Backtracking")
        ct_bt = time.perf_counter()
        et_bt = round(ct_bt - st_bt, 5)

        return render_template(
            "index.html",
            graph_generated=True,
            rows=rows,
            cols=cols,
            et_gr=et_gr,
            et_bt=et_bt,
            matrix=adj_matrix,
        )
    except Exception as e:
        return render_template(
            "index.html", graph_generated=False, error=str(e), rows=rows, cols=cols
        )


@app.route("/graph")
def graph():
    return send_file("static/graph.png", mimetype="image/png")


@app.route("/about-us")
def about_us():
    with open("authors.json", "r") as file:
        authors = json.load(file)

    return render_template("about-us.html", authors=authors)


if __name__ == "__main__":
    app.run(debug=True)
