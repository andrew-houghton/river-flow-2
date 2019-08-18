import networkx as nx


class HeightGraph(nx.DiGraph):
    def __init__(self, height_map):
        super().__init__()
        self._insert_height_map_edges(height_map)

    def _insert_height_map_edges(self, height_map):
        for y, row in enumerate(height_map):
            for x, item in enumerate(row):
                self.add_node((y, x))
                nx.set_node_attributes(self, {(y, x): {"height": item}})

                if (y - 1, x) in self:
                    self.add_edge((y - 1, x), (y, x))
                    self.add_edge((y, x), (y - 1, x))
                if (y, x - 1) in self:
                    self.add_edge((y, x - 1), (y, x))
                    self.add_edge((y, x), (y, x - 1))

    def merge_equal_height_nodes(self):
        pass
