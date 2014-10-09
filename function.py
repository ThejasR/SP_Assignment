import csv
# using python3

def two():
	#performs upgrade from assign 2 csv file to assign 3
	db = []
	reader = csv.reader(open('Country.csv', 'r'))
	for row in reader:
		if row==0:
		    db.append("Country,Capital,Population")
		else:
		    db.append(row)

	for i in range(0,len(db)):
		if i==0:
		    db[0].append("Language")
		else:
		    db[i].append("English")
		    
	with open('Country.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(db)



