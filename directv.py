###############################################################
###
###   DirecTV python class
###
###############################################################

#import socket # for connecting with ip devices
#import chardet
#import time
import urllib2
import json

# data object
class Observable:
    def __init__(self, initialValue=None):
        self.data = initialValue
        self.callbacks = {}

    def addCallback(self, func):
        self.callbacks[func] = 1

    def delCallback(self, func):
        del self.callback[func]

    def _docallbacks(self):
        for func in self.callbacks:
             func(self.data)

    def set(self, data):
        self.data = data
        self._docallbacks()

    def get(self):
        return self.data

    def unset(self):
        self.data = None

# directv instance of the observable class
class DirecTV(Observable):
    def __init__(self,ipaddy):
        Observable.__init__(self)
        self.ipaddy=ipaddy
        self.port=8080
        self.power=0
        self.channel=0
        self.getpower()
        self.getchan()

    def buildurl(self,cmd):
        return "http://"+self.ipaddy+':'+str(self.port)+cmd

    def geturl(self,url):
        try:
            content=urllib2.urlopen(url).read()
            return content
        except urllib2.HTTPError, e:
            return None
        except urllib2.URLError, e:
            return None
        except Exception:
            return None

    def getjson(self,response):
        if response:
            return json.loads(response)
        else:
            return None

    def getpower(self):
        data=self.getjson(self.geturl(self.buildurl('/info/mode?clientAddr=0')))
        if data:
            self.power = 1 - data['mode']
            #print 'POWER:'+str(self.power)

    def getchan(self):
        data=self.getjson(self.geturl(self.buildurl('/tv/getTuned?clientAddr=0&videoWindow=primary')))
        if data:
            self.channel = data['major']
            #print 'CHANNEL:'+str(self.channel)

    def sendkey(self,key,pressType):
        # keys: power, poweron, poweroff, format, pause, rew, replay, stop, advance, ffwd, record, play, guide, active, list, exit, back, menu, info,
        #       up, down, left, right, select, red, green, yellow, blue, chanup, chandown, prev, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, dash, enter
        # http://STBIP:port/remote/processKey?key=string[&hold=string][&clientAddr=string]
        data=self.getjson(self.geturl(self.buildurl('/remote/processKey?key='+key+'&hold='+pressType+'&clientAddr=0')))

    def sendchan(self,chan,minor):
        # http://STBIP:port/tv/tune?major=num[&minor=num][&clientAddr=string]
        chanstring=str(chan)
        if minor>0:
            chanstring=chanstring+'&minor='+str(minor)
        data=self.getjson(self.geturl(self.buildurl('/tv/tune?major='+chanstring+'&clientAddr=0')))

    def sendpower(self,power):
        pwr=['poweroff','poweron']
        self.sendkey(pwr[power])

#dtv = DirecTV("192.168.88.253")
#dtv.sendkey('guide','keyPress')
#dtv.sendchan(11,0)
#dtv.sendpower(1)