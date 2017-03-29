import matplotlib.pyplot as plt
class Graph():

	def __init__(self,func=lambda x: x):
		self.func = func
		
	def Plot(self):
		x = range(1,10)
		y = [self.func(i) for i in x]
		
		plt.plot(x, y)
		plt.show()


