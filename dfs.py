class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")

    def __str__(self):
        cur = self.head.next
        out = ""
        sep = "->"
        while cur is not None:
            out += f"{cur.value}{sep}"
            cur = cur.next
        out = out[:-2]
        return out

    def push(self, value):
        new_element = Node(value)
        new_element.next = self.head.next
        self.head.next = new_element

    def pop(self):
        if self.head.next is None:
            #print("Стек пуст")
            return None
        tmp = self.head.next.value
        self.head.next = self.head.next.next
        return tmp

class PersistentStack(Stack):
    def __init__(self):
        self.backups = []
        super().__init__()

    def create_backup(self):
        tmp = PersistentStack()
        tmp.head = self.head
        self.backups.append(tmp)

    def get_backup(self, i):
        return self.backups[i]

    def push(self, value):
        self.create_backup()
        super().push(value)

    def pop(self):
        self.create_backup()
        return super().pop()

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append(end)

    def dfs_with_cycle_detection(self, start, visited=None, stack=None):
        if visited is None:
            visited = set()
        if stack is None:
            stack = PersistentStack()

        if start in visited:
            # Вывод цикла
            while stack.head.next.value != start:
                print(stack.pop(), end=" -> ")
            print(start)
            return

        visited.add(start)
        stack.push(start)

        for neighbor in self.graph.get(start, []):
            self.dfs_with_cycle_detection(neighbor, visited, stack)

        stack.pop()

    def count_paths_dag(self, start, end, visited=None):
        if visited is None:
            visited = set()

        if start == end:
            return 1

        visited.add(start)
        paths = 0

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                paths += self.count_paths_dag(neighbor, end, visited)

        visited.remove(start)
        return paths

# Пример использования
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'A')

print("DFS with cycle detection:")
graph.dfs_with_cycle_detection('A')

dag_graph = Graph()
dag_graph.add_edge('A', 'B')
dag_graph.add_edge('A', 'C')
dag_graph.add_edge('B', 'D')
dag_graph.add_edge('C', 'D')
dag_graph.add_edge('D', 'E')

start_node = 'A'
end_node = 'E'
num_paths = dag_graph.count_paths_dag(start_node, end_node)
print(f"Number of paths from node {start_node} to node {end_node} in the DAG: {num_paths}")