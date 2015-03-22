import csv
import string

count = 0
fileReadIn = open('sent-emails-2-gai-2.csv', 'rb')

fileWriteTo = open('output.csv', 'wb')
writer = csv.writer(fileWriteTo, dialect='excel')

writer.writerow(['date', 'hour', 'dayofmonth', 'month', 'year', 'weekday', 'from', 'to'])

for line in fileReadIn.readlines():
	line = line.strip('\n')
	line = line.replace('"', '')
	row = line.split(',')

	dateCol = row[0]
	fromCol = row[1]
	toCol = row[2]
	
	if "@" in dateCol or ",," in dateCol or "=" in toCol:
		continue

	dateRow = dateCol.split(' ')
	weekday = dateRow[0]
	day = dateRow[1]
	month = dateRow[2]
	year = dateRow[3]
	hour = dateRow[4]
	hour = hour[0:2]

	if month == "Jan":
		month = 1
	elif month == "Feb":
		month = 2
	elif month == "Mar":
		month = 3
	elif month == "Apr":
		month = 4
	elif month == "May":
		month = 5
	elif month == "Jun":
		month = 6
	elif month == "Jul":
		month = 7
	elif month == "Aug":
		month = 8
	elif month == "Sep":
		month = 9
	elif month == "Oct":
		month = 10
	elif month == "Nov":
		month = 11
	elif month == "Dec":
		month = 12

	###
	if "ertini@" in fromCol:
		fromCol = "Enrico Bertini"

	###
	if "<" in toCol and ">" in toCol:
		rcvCount = toCol.count("<", 0, len(toCol))
		# print rcvCount

		partOfToCol = toCol.split('> ')

		i = 0
		nameList = []

		while i < rcvCount:
			tmp = partOfToCol[i].split(' <')
			# print tmp[0]

			if "'" in tmp[0]:
				# print tmp
				tmp[0] = tmp[0].replace("'", "\\\'")
			
			nameList.append(tmp[0])
			# print nameList[i]

			# print (row[0], hour, day, month, year, weekday, fromCol, nameList[i])
			writer.writerow([row[0], hour, day, month, year, weekday, fromCol, nameList[i]])

			i += 1

	else:
		continue

	count += 1

fileReadIn.close()
print (count + 1)