#PLACE YOUR CODE HERE

a = open("/Users/georgemcintire/ds/metis/prework/dsp/python/faculty.csv", "r")

f = a.read()

w = f.split("\n")


faculty = []

for i in w:
	split_row = i.split(",")
	faculty.append(split_row)
	

faculty_dict = {}

faculty2 = faculty[1:]

for i in range(len(faculty2)):
	faculty_dict[faculty[i][0]] = faculty[i][1:]

import itertools

def printnelementsfromdict(n, dict):
	n_items = list(itertools.islice(dict.items(),n))
	for item in n_items:
		print item
print printnelementsfromdict(3, faculty_dict)
	
faculty_dict2 = {}

for i in range(len(faculty)):
	faculty_dict2[tuple(faculty[i][0].split(" "))] = faculty[i][1:]
	
print printnelementsfromdict(3, faculty_dict2)

ordered_prof_dict = sorted(faculty_dict2.items(), key = lambda x: x[0][-1])

for i in ordered_prof_dict[:3]:
	print i


