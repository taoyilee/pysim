class diode:
    def __init__(self, inst_name, node1, node2, value):
        self.inst_name = inst_name
        self.node1 = node1
        self.node2 = node2
        self.value = value
 
    def __str__(self):
        return 'Inductor ({0}, {1}, {2}, {3})'.format(
            self.inst_name, self.node1, self.node2, self.value)
