a = open("/Users/georgemcintire/ds/metis/prework/dsp/python/faculty.csv", "r")
b = open("/Users/georgemcintire/ds/metis/prework/dsp/python/emails.csv", "w")


f = a.read()


w = f.split("\n")

faculty = []

for i in w:
	split_row = i.split(",")
	faculty.append(split_row)

#print faculty


emails = []

for i in faculty[1:]:
	emails.append(i[3])

import csv 
wr = csv.writer(b, quoting=csv.QUOTE_ALL)
wr.writerow(emails)
