import os
import urllib2
from time import sleep

url="http://pause.games/pulse"

def internet_on():
    try:
        # print "trying connecting to: ", url
        urllib2.urlopen(url, timeout=5)
        # print "success"
        return True
    except urllib2.URLError as err:
        # print "failed"
        return False

while True:
    sleep(1)
    if internet_on():
        if os.path.isfile("/tmp/signal1"):
            os.remove("/tmp/signal1")
            print "network connection restored."
    else:
        if not os.path.isfile("/tmp/signal1"):
            open("/tmp/signal1", 'a').close()
            print "network connection lost."     
