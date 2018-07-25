class DigiNode:

    def __init__(self, **kwargs):
        self.id    = kwargs["dId"]
        self.code  = kwargs["dCode"]
        self.gene  = kwargs["dGene"]
        self.name  = kwargs["dName"]
        self.stage = kwargs["dStage"]
        self.type  = kwargs["dType"]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
