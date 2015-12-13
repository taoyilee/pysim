class bjt:
    def __init__(self, inst_name, node1, node2, node3, value):
        self.inst_name = inst_name
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.value = value
 
    def __str__(self):
        return 'BJT ({0}, {1}, {2}, {3}, {4})'.format(
            self.inst_name, self.node1, self.node2, self.node3, self.value)
