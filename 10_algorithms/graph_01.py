# W dowolny sposób ponumeruj wierzchołki grafu miasteczka:
# 1. Korzystając z dowolnej metody reprezentacji grafu zapisać istniejące połączenia pomiędzy budynkami.
# 2. Wyświetl wszystkie krawędzie parami, podzielone za pomocą ---

vertex_list = {
    1: "dom",
    2: "szkoła",
    3: "kościół",
    4: "bar",
    5: "szpital",
    6: "kino",
    7: "teatr",
}

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 4, 6],
    4: [1, 3, 5],
    5: [2, 4, 6, 7],
    6: [3, 5, 7],
    7: [5, 6]
}

for start_vertex, neighbours in graph.items():
    for n in neighbours:
        print(f"{vertex_list[start_vertex]} --- {vertex_list[n]}")
