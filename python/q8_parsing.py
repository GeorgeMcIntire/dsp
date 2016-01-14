#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


rawfootball = open("/Users/georgemcintire/ds/metis/prework/dsp/python/football.csv", "r")

readfootball = rawfootball.read()

footballrows = readfootball.split('\n')


full_data = []

for i in footballrows:
	splitrow = i.split(",")
	full_data.append(splitrow)

full_data2 = full_data[1:]	

goaldiff = []

for i in full_data2:
	goaldiff.append(int(i[5]) - int(i[6]))


worstgoaldiff = min(goaldiff)

for i in full_data2:
	if int(i[5]) - int(i[6]) == worstgoaldiff:
		print i[0]





