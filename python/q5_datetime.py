# Hint:  use Google to find python function

####a) 
from datetime import datetime 

date_start1 = '01-02-2013'  
date_stop1 = '07-28-2015'   

date_format1 = "%m-%d-%Y"


start1 = datetime.strptime(date_start1, date_format1)
end1 = datetime.strptime(date_stop1, date_format1)

print end1 - start1


####b)  
from datetime import datetime

date_start2 = '12312013'  
date_stop2 = '05282015'
date_format2 = "%m%d%Y"

start2 = datetime.strptime(a, date_format2)
end2 = datetime.strptime(b, date_format2)

print end2 - start2 

####c)  
from datetime import datetime
a = '15-Jan-1994'  
b = '14-Jul-2015'  
date_format3 = "%d-%b-%Y"
start3 = datetime.strptime(a, date_format3)
end3 = datetime.strptime(b, date_format3)

print end3 - start3
