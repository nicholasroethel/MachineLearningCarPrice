import csv

with open('craigslistVehiclesFull.csv','r') as whole_file:
	original_csv_reader = csv.reader(whole_file)

	with open('craigsListVehiclesLA.csv','w') as la_file:
		csv_writer = csv.writer(la_file)

		for line in original_csv_reader:
			if line[1] == 'losangeles':
				csv_writer.writerow(line)


