import requests, time

def getIP(): # GET IP
    result = requests.get("http://ipinfo.io/ip")
    return result.text

def checkIP():
    initial = getIP() # START
    print(f'Initial IP: {initial}')
    while True:
        current = getIP()
        if initial == current: # CHECK
            print("Nice, sleep for 1 min")
            time.sleep(60)
            pass                                
        else:
            print("IP has changed!")

print('CHECKIN`')
checkIP()