import networkx as nx


class HeightGraph(nx.DiGraph):
    def __init__(self, height_map):
        super().__init__()
        self._insert_height_map_edges(height_map)

    def insert_node_with_edges(self, row_num, col_num):
        self.add_node((row_num, col_num))
        if (row_num - 1, col_num) in self:
            self.add_edge((row_num - 1, col_num), (row_num, col_num))
            self.add_edge((row_num, col_num), (row_num - 1, col_num))
        if (row_num, col_num - 1) in self:
            self.add_edge((row_num, col_num - 1), (row_num, col_num))
            self.add_edge((row_num, col_num), (row_num, col_num - 1))

    def _insert_height_map_edges(self, height_map):
        node_heights = {}
        for row_num, row in enumerate(height_map):
            for col_num, height in enumerate(row):
                self.insert_node_with_edges(row_num, col_num)
                node_heights[(row_num, col_num)] = {"height": height}
        nx.set_node_attributes(self, node_heights)

    def merge_equal_height_nodes(self):
        edges = self.edges()
        for u, v in edges:
            if self.has_edge(u, v):
                if self.nodes[u]["height"] == self.nodes[v]["height"]:
                    self.merge_nodes(u, v)

    def merge_nodes(self, u, v):
        print(u, v)
        pass
