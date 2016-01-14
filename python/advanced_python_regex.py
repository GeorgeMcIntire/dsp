a = open("/Users/georgemcintire/ds/metis/prework/dsp/python/faculty.csv", "r")

f = a.read()

w = f.split("\n")


faculty = []

for i in w:
	split_row = i.split(",")
	faculty.append(split_row)
	
faculty2 = faculty[1:]

degrees = []

for i in faculty2:
	degrees.append(i[1])
	
degreedict = {}

for i in degrees:
	if i not in degreedict:
		degreedict[i] = 1
	elif i in degreedict:
		degreedict[i] += 1

titles = []
for i in faculty2:
	titles.append(i[2])
	
titlesdict = {}

for i in titles:
	if i not in titlesdict:
		titlesdict[i] = 1
	elif i in titlesdict:
		titlesdict[i] += 1

print len(degreedict)
print degreedict

print len(titlesdict)
print titlesdict

emails = []

for i in faculty2:
	emails.append(i[3])

emaildomains = []

for i in emails:
	emaildomains.append(i[i.index("@"):])
print set(emaildomains)

