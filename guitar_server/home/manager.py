import serial
import serial.tools.list_ports
import time
import thread
from datetime import datetime,timedelta

'''
g_singleton = None
def getObj():
    if g_singleton is not None:
        print 'singleton is working'
        return g_singleton
    else:
        g_singleton = manager()
        return g_singleton
'''

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance

@singleton
class manager():

    port = ""
    ser = serial.Serial()


    def __init__(self):
        print 'creating manger!!!'
        self.lastFire = None
        ports = list(serial.tools.list_ports.comports())
        if not ports:
            raise Exception("can't find serial port")


        for idx in range(len(ports)):
            pDict = ports[idx]
      

            
            if pDict[1].find("Digispark Serial") >= -1:
                print pDict[1]
                self.port = pDict[0]
                self.ser = serial.Serial(self.port)

            if self.port == "":
                raise Exception("can't find serial port")
            else:
                thread.start_new_thread(self.beat, ())
                pass

    def shouldFire(self):
        if self.lastFire is None:
            self.lastFire = datetime.now()
            return True

        total = (datetime.now() - self.lastFire)
        if total.total_seconds()>2:
            print "total:"+str(total.total_seconds())
            self.lastFire = datetime.now()
            return True
        else: 

            return False



    def onFails(self):
        if self.shouldFire():
            self.ser.write(b'1')  # write a string
            time.sleep(1)
        



    def beat(self):
        self.ser.write(b'0')  # write a string
        time.sleep(1)
        pass


    def close(self):
        self.ser.close()
        pass




if __name__ == "__main__":

    try:
        m = manager()
 


        #m.close()             # close port
    except Exceptioy, exp:
        print exp
