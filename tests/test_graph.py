from hypothesis import given
from hypothesis import strategies as st
from flow.graph import HeightGraph


@st.composite
def height_map_strategy(draw):
    width = draw(st.integers(min_value=1, max_value=200))
    rows = st.lists(st.integers(), min_size=width, max_size=width)
    return draw(st.lists(rows, min_size=1))


@given(height_map_strategy())
def test_heightmap_strategy(height_map):
    assert type(height_map) == list
    assert type(height_map[0]) == list
    assert type(height_map[0][0]) == int
    assert len({len(i) for i in height_map}) == 1 # Only on size for rows


@given(height_map_strategy())
def test_convert_to_graph(height_map):
    g = HeightGraph(height_map)

    print(height_map)
    print(len(g))
