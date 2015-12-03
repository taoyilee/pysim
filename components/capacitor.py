class capacitor:
    def __init__(self, inst_name, node1, node2, value, is_g2):
        self.inst_name = inst_name
        self.node1 = node1
        self.node2 = node2
        self.value = value
        self.is_g2 = is_g2
 
    def __str__(self):
        return 'Capacitor ({0}, {1}, {2}, {3}, {4})'.format(
            self.inst_name, self.node1, self.node2, self.value, self.is_g2)
