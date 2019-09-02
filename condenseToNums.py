import csv
#gets rid of all columns that dont have numbers
with open("craigslistVehiclesLA.csv","r") as original:
    reader = csv.reader(original)
    with open("LAVerhiclesCondensed.csv","w") as modified:
        writer= csv.writer(modified)
        for row in reader:
            writer.writerow((row[3], row[9], row[18], row[19], row[20], row[22], row[25],row[2]))