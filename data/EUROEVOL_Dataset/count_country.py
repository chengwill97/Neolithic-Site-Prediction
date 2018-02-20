import csv

import collections

csv_name = '/Users/WillC/Documents/Rutgers/3rd_Year/Spring_Semester/Intro_Data_Science/Project/data/EUROEVOL_Dataset/EUROEVOL09-07-201516-34_CommonSites.csv'

countries = list()

with open(csv_name) as csv_file:
	reader = csv.reader(csv_file, delimiter = ',')
	for row in reader:
		countries.append(row[0])

count = collections.Counter(countries)

for common in count.most_common():
	print common