import networkx as nx

class HeightGraph(nx.Graph):
    def __init__(self, height_map):
        super().__init__()
        self._insert_height_map_edges(height_map)

    def _insert_height_map_edges(self, height_map):
        for y, row in enumerate(height_map):
            for x, item in enumerate(row):
                self.add_node((y,x))
                nx.set_node_attributes(self, {(y,x): {'height': item}})
