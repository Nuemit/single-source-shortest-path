#   sssp    [0][0]
#                 [0]:
#            I  J  L
#            node indicator
#               path indicator
#                  length of path to nodes, len(sssp[i][j][l]) must be same as len(sssp[i][j])
#
#            if (len(sssp[i][j][l]) != len(sssp[i][j][l])):
#               return ["error: XX", "bad length of paths", "paths must have same length as path indicators exist"]


class single_source_shortest_path:
    def __init__(self):
        """class for sssp"""
        self.node_names = []
        self.node_dict = {}

    def gen_content_table(self, nodes: int):
        """generates tables with content for n nodes"""
        for n in nodes:
            self.nodenames.append(f"Node-{n}")


    def gen_path_length(self, nodes: int, minlength: int, maxlength: int):
        """generate path length for n nodes"""
        pass

