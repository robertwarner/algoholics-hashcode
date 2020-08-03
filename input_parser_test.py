import os

from input_parser import VideoServiceNetwork


def inputParserTest():
    graph = VideoServiceNetwork('./data/example.in')
    print(graph.endpoint_graph)
    for f in os.listdir('./data/'):
        _ = VideoServiceNetwork('./data/' + f)
