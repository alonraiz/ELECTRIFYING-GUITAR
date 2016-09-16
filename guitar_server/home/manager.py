import serial
import serial.tools.list_ports
import time
import thread



class manager():

    port = ""
    ser = serial.Serial()

    def __init__(self):
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

    def onFails(self):
        self.ser.write(b'1')  # write a string
        time.sleep(1)
        pass



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
    except Exception, exp:
        print exp
