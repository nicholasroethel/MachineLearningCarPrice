import csv
#gets rid columns not selected by RFE
with open("LAVerhiclesCondensed.csv","r") as original:
    reader = csv.reader(original)
    with open("LAVerhiclesRFE.csv","w") as modified:
        writer= csv.writer(modified)
        writer.writerow(['year','odometer','country_fips','price'])
        for row in reader:
            writer.writerow((row[0],row[1],row[4],row[7]))