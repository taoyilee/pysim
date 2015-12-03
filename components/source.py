class voltage_source:
    def __init__(self, inst_name, node1, node2, value):
        self.inst_name = inst_name
        self.node1 = node1
        self.node2 = node2
        self.value = value
 
    def __str__(self):
        return 'Voltage Source ({0}, {1}, {2}, {3})'.format(
            self.inst_name, self.node1, self.node2, self.value)

class inductor:
    def __init__(self, inst_name, node1, node2, value):
        self.inst_name = inst_name
        self.node1 = node1
        self.node2 = node2
        self.value = value
 
    def __str__(self):
        return 'Inductor ({0}, {1}, {2}, {3})'.format(
            self.inst_name, self.node1, self.node2, self.value)

class current_source:
    def __init__(self, inst_name, node1, node2, value, is_g2):
        self.inst_name = inst_name
        self.node1 = node1
        self.node2 = node2
        self.value = value
        self.is_g2 = is_g2
 
    def __str__(self):
        return 'Current Source ({0}, {1}, {2}, {3}, {4})'.format(
            self.inst_name, self.node1, self.node2, self.value, self.is_g2)
class resistor:
    def __init__(self, inst_name, node1, node2, value, is_g2):
        self.inst_name = inst_name
        self.node1 = node1
        self.node2 = node2
        self.value = value
        self.is_g2 = is_g2
 
    def __str__(self):
        return 'Resistor ({0}, {1}, {2}, {3}, {4})'.format(
            self.inst_name, self.node1, self.node2, self.value, self.is_g2)
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
