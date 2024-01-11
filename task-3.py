# Реалізуємо алгоритм Дейкстри 

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

# Приклад графа у вигляді словника

graph = {
      "Київ": {"мацква" : 12, "1" : 2, "3" : 3},
       "1": {"Київ" : 2, "2" : 10},
       "2": {"1" : 10, "мацква": 1},
       "3": {"Київ" : 3, "4" : 1},
       "4": {"3" : 1, "5" : 4},
       "5": {"4" : 4, "мацква": 2},
       "мацква": {"Київ" : 12, "2" : 1, "5" : 2}
    }
# Виклик функції для вершини A
print("Алгоритм Дейкстри, знаходження найкоротшого шляху для графу:")
print(dijkstra(graph, "Київ"))

