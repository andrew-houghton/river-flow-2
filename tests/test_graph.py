from hypothesis import given, example
from hypothesis import strategies as st
from flow.graph import HeightGraph


@st.composite
def height_map_strategy(draw):
    width = draw(st.integers(min_value=1, max_value=200))
    rows = st.lists(st.integers(min_value=-100, max_value=2000), min_size=width, max_size=width)
    return draw(st.lists(rows, min_size=1))


@given(height_map_strategy())
def test_heightmap_strategy(height_map):
    assert type(height_map) == list
    assert type(height_map[0]) == list
    assert type(height_map[0][0]) == int
    assert len({len(i) for i in height_map}) == 1  # Only on size for rows


@given(height_map_strategy())
@example(height_map=[[0, 0]])
def test_convert_to_graph(height_map):
    g = HeightGraph(height_map)

    assert len(g) > 0
    check_nodes_have_height(g)
    check_connected(g, height_map)
    check_connected_in_order(g, height_map)

    # g.merge_equal_height_nodes()
    # check_no_equal_height_edges(g)


def check_nodes_have_height(graph):
    for node in graph.nodes:
        assert type(graph.nodes[node]['height']) == int


def check_connected(graph, height_map):
    for row_num, row in enumerate(height_map):
        for col_num in range(len(row)):
            if row_num > 0:
                assert graph.has_edge((row_num, col_num), (row_num - 1, col_num))
            if col_num > 0:
                assert graph.has_edge((row_num, col_num), (row_num, col_num - 1))


def check_no_equal_height_edges(graph):
    for u, v in graph.edges:
        u_height = graph[u]["height"]
        v_height = graph[v]["height"]
        assert u_height != v_height


def check_connected_in_order(graph, height_map):
    lowest_height = min([min(r) for r in height_map])
    highest_height = max([max(r) for r in height_map])

    lowest = graph.lowest_node_key
    highest = graph.highest_node_key

    assert graph.nodes[lowest]['height'] == lowest_height
    assert graph.nodes[highest]['height'] == highest_height

    count = 1
    while graph.nodes[lowest]["next"] != None:
        lowest = graph.nodes[lowest]["next"]
        count += 1

    assert count == graph.number_of_nodes()
