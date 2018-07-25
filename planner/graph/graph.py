from graph.node import DigiNode
from util.common import *

class DigiGraph:

    def __init__(self):
        self.nodes = self.buildNodes()

    def buildNodes(self):
        r_nodes = self.readData("graph/data/r_data.txt", ROOKIE)
        c_nodes = self.readData("graph/data/c_data.txt", CHAMPION)
        u_nodes = self.readData("graph/data/u_data.txt", ULTIMATE)
        m_nodes = self.readData("graph/data/m_data.txt", MEGA)
        return { **r_nodes, **c_nodes, **u_nodes, **m_nodes }

    def readData(self, data_fn, stage):
        nodes = {}
        digiType = -1
        with open(data_fn,"r") as data:
            for line in data:
                if line.startswith("##"):
                    digiType += 1
                elif line.startswith("$$$"):
                    break
                else:
                    line_arr = line.strip().split(":")
                    node = DigiNode(**{
                        "dId"    : int(line_arr[INDEX_ID]),
                        "dCode"  : line_arr[INDEX_CODE],
                        "dGene"  : line_arr[INDEX_GENE],
                        "dName"  : line_arr[INDEX_NAME],
                        "dStage" : stage,
                        "dType"  : digiType})
                    nodes[int(line_arr[INDEX_ID])] = node
            return nodes
