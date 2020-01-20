import csv

class CSV:

	
	def __init__(self):
		self.output = list()

	def getData(self):
		return self.output

	def readcsv(self):
		info_csv = csv.reader(open('routes.csv', newline=''), delimiter=' ', quotechar='|')
		for row in info_csv:
			x = (', '.join(row))
			self.output.append(x)



