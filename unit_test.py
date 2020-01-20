import unittest
from quiz_test import Routes
import csv
import  read_csv

quizMap = Routes()
csvfile = read_csv.CSV()
csvfile.readcsv()
data = csvfile.getData()

for val in data:
	values = val.split(",")
	quizMap.add(values[0],values[1],int(values[2]))

class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		expect = "Your trip from A to D includes 0 stops and will take 15 minutes."
		result = str(quizMap.findPaths("A", "D"))
		self.assertEqual(result, expect)

if __name__ == '__main__':
	unittest.main()


