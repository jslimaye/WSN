def connection(x,y):
	from urllib.request import urlopen
	from time import sleep
	baseURL = "https://api.thingspeak.com/update?api_key=5LVY79J2X9WBEOR9"
	
	conn = urlopen(baseURL + '&field1=%s&field2=%s' % (x,y))
	print(conn.read())
	
	sleep(1)
	conn.close()

	return



	
