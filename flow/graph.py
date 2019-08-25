import networkx as nx


class HeightGraph(nx.DiGraph):
    def __init__(self, height_map):
        super().__init__()
        self.height = len(height_map)
        self.width = len(height_map[0])
        nx.generators.lattice.grid_2d_graph(self.height, self.width, create_using=self)
        self._set_node_heights(height_map)
        self._create_height_order_list()

    def _set_node_heights(self, height_map):
        node_heights = {}
        for row_num, row in enumerate(height_map):
            for col_num, height in enumerate(row):
                node_heights[(row_num, col_num)] = {"height": height}
        nx.set_node_attributes(self, node_heights)

    def _create_height_order_list(self):
        height_order_nodes = sorted(self.nodes(), key=lambda x: self.nodes[x]["height"])
        for i in range(len(height_order_nodes)):
            node = self.nodes[height_order_nodes[i]]

            if i > 0:
                node["prev"] = height_order_nodes[i-1]
            else:
                node["prev"] = None

            if i < len(height_order_nodes) - 1:
                node["next"] = height_order_nodes[i+1]
            else:
                node["next"] = None

        self.lowest_node_key = height_order_nodes[0]
        self.highest_node_key = height_order_nodes[-1]

    def merge_equal_height_nodes(self):
        edges = self.edges()
        for u, v in edges:
            if self.has_edge(u, v):
                if self.nodes[u]["height"] == self.nodes[v]["height"]:
                    self.merge_nodes(u, v)

    def merge_nodes(self, u, v):
        pass

