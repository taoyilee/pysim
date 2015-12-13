import numpy as np

class Abpair:
	def __init__(self, A, b):
		self.A = A
		self.b = b
	def solve(self):
		return np.linalg.solve(self.A, self.b)
