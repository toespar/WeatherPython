#To make ascii tables with colour and some features
from __future__ import print_function
from terminaltables import AsciiTable, DoubleTable
from colorclass import Color, Windows
#Module to make an url connection
from urllib2 import urlopen
#Module to parse json response
import json

def weatherTable(city, country=None):
		if(country == None):
			request = urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric')
		else:
			request = urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+','+country+'&units=metric')
		
		response = json.loads(request.read())
		weather = response['weather'][0]['description']
 
		current_temp = str(response['main']['temp']) 
		wind = str(response['wind']['speed']) 
		clouds = str(response['clouds']['all'])
		pressure = str(response['main']['pressure'])
		humidity = str(response['main']['humidity'])


		table_data = [
			[Color('{autoyellow}Current temp.{/autoyellow}'), Color('{autoyellow}Wind{/autoyellow}'),Color('{autoyellow}Cloudiness{/autoyellow}'),Color('{autoyellow}Pressure{/autoyellow}'),Color('{autoyellow}Humidity{/autoyellow}'),Color('{autoyellow}Description{/autoyellow}')],
			[str(current_temp)+" "+u"\N{DEGREE SIGN}"+"C", str(wind)+" km/h", str(clouds)+" %",str(pressure)+" hPa", str(humidity)+"%", str(weather)]
]

		table = DoubleTable(table_data, city.capitalize())
		table.inner_row_border = True
		table.justify_columns[0] = 'center'
		table.justify_columns[1] = 'center'
		table.justify_columns[2] = 'center'
		table.justify_columns[3] = 'center'
		table.justify_columns[4] = 'center'
		table.justify_columns[5] = 'center'
		return(table.table)

print ()
print  ("		#    # ######   ##   ##### #    # ###### #####\n"  
		"		#    # #       #  #    #   #    # #      #    #\n" 
		"		#    # #####  #    #   #   ###### #####  #    #\n" 
		"		# ## # #      ######   #   #    # #      #####\n"  
		"		##  ## #      #    #   #   #    # #      #   #\n"  
		"		#    # ###### #    #   #   #    # ###### #    #\n")


while (True):
	print("---OPTIONS---")
	print("1. Default location (Valencia,ES)")
	print("2. Show other locations")
	number = raw_input("Your choice: ")
	number = int(number)
	print()
	if number == 1:
		print (weatherTable("valencia","es"))
		break
	elif number == 2:
		print ("->Write city,country<-")
		print("Example: Valencia,ES")
		location = raw_input("Choose location: ")
		location = location.split(",")
		print (str(len(location)))
		if len(location) >= 2:
			print (weatherTable(location[0], location[1]))
		elif len(location) == 1:
			print (weatherTable(location[0]))
			
		break
	else:
		print ("Option not available. Try it again")