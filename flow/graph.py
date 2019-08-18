import networkx as nx


class HeightGraph(nx.DiGraph):
    def __init__(self, height_map):
        super().__init__()
        self.height = len(height_map)
        self.width = len(height_map[0])
        nx.generators.lattice.grid_2d_graph(self.height, self.width, create_using=self)
        self._set_node_heights(height_map)

    def _set_node_heights(self, height_map):
        node_heights = {}
        for row_num, row in enumerate(height_map):
            for col_num, height in enumerate(row):
                node_heights[(row_num, col_num)] = {"height": height}
        nx.set_node_attributes(self, node_heights)

    def merge_equal_height_nodes(self):
        edges = self.edges()
        for u, v in edges:
            if self.has_edge(u, v):
                if self.nodes[u]["height"] == self.nodes[v]["height"]:
                    self.merge_nodes(u, v)

    def merge_nodes(self, u, v):
        print("merging", u, v)
        pass

