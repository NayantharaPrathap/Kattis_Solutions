from collections import deque

class ConnectedGraph:
    def __init__(self):
        self.next_index = 0
        self.names = []
        self.vertices = {}
        self.edges = {}
        self.rev_edges = {}
        self.vertices_visited = set()
        self.changed = -1

    def depth_first_search(self):
        stack = deque([self.changed])
        while stack:
            curr = stack.pop()
            if curr in self.vertices_visited:
                continue
            self.vertices_visited.add(curr)
            for v in self.edges[curr]:
                stack.append(v)

    def dependencies(self):
        stack = deque([(-1, self.changed)])
        while stack:
            parent,curr = stack.pop()
            if parent != -1:
                self.rev_edges[curr].remove(parent)
                if any(i in self.vertices_visited for i in self.rev_edges[curr]):
                    continue
            print(self.names[curr])
            for v in self.edges[curr]:
                stack.append((curr,v))

    def add_dependencies(self, source, dest):
        if source not in self.vertices:
            self.names.append(source)
            self.vertices[source] = self.next_index
            self.edges[self.next_index] = set()
            self.rev_edges[self.next_index] = set()
            self.next_index += 1
        j = self.vertices[source]
        for ele in dest:
            if ele not in self.vertices:
                self.names.append(ele)
                self.vertices[ele] = self.next_index
                self.edges[self.next_index] = set()
                self.rev_edges[self.next_index] = set()
                self.next_index += 1
            k = self.vertices[ele]
            self.edges[k].add(j)
            self.rev_edges[j].add(k)

    def change(self, source):
        self.changed = self.vertices[source]
        
def main():
    g = ConnectedGraph()
    for _ in range(int(input())):
        dest,*source = input().split()
        g.add_dependencies(dest[:-1], source)
    g.change(input().rstrip())
    g.depth_first_search()
    g.dependencies()
    
if __name__ == "__main__":
    main()
