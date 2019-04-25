def connection(x,y):
    from urllib.request import urlopen
    from time import sleep
    baseURL = "https://api.thingspeak.com/update?api_key=5LVY79J2X9WBEOR9"
    
    conn = urlopen(baseURL + '&field1=%f&field2=%f' % (x,y))
    print(conn.read())
    
    sleep(1)
    conn.close()

    return

def conn2(x,y):
    from urllib.request import urlopen
    from time import sleep
    baseURL = "https://api.thingspeak.com/update?api_key=5LVY79J2X9WBEOR9"
    
    conn = urlopen(baseURL + '&field3=%f&field4=%f' % (x,y))
    print(conn.read())
    
    sleep(1)
    conn.close()

    return

    
