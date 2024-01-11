# Рекурсивна реалізація алгоритму DFS 

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# Рекурсивна реалізація BFS

from collections import deque

def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)


def main():
    graph = {
      "Київ": ["мацква", "1", "3"],
       "1": ["Київ", "2"],
       "2": ["1", "мацква"],
       "3": ["Київ", "4"],
       "4": ["3", "5"],
       "5": ["4", "мацква"],
       "мацква": ["Київ", "2", "5"]
    }

    print("Знаходження шляхів у графі, алгоритм BFS:\n")
    bfs_recursive(graph, deque(["Київ"]))
    print("\n")
    print("Знаходження шляхів у графі, алгоритм DFS:\n")
    dfs_recursive(graph, "Київ")
    print("\n")


if __name__ == "__main__":
    main()