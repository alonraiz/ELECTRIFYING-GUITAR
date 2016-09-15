import serial
import serial.tools.list_ports
import time
import thread





class manager():

    port = ""
    ser = serial.Serial()

    def __init__(self):
        ports = list(serial.tools.list_ports.comports())

        for idx in range(len(ports)):

            pDict =ports[idx]
            if pDict.product == "Digispark Serial":
                print pDict.device
                self.port = pDict.device
                self.ser = serial.Serial(self.port)

            if self.port == "":
                raise Exception("can't find serial port")
            else:
                thread.start_new(self.beat, ())

    def onFails(self):
        ser.write(b'1')  # write a string
        time.sleep(1)
        pass



    def beat(self):
        ser.write(b'0')  # write a string
        time.sleep(1)
        pass




try:




    ser = serial.Serial(port)  # open serial port
    print(ser.product)         # check which port was really used

    while True:
        ser.write(b'0')     # write a string
        time.sleep(1)
        ser.write(b'1')  # write a string
        time.sleep(1)


    ser.close()             # close port
except Exception, exp:
    print exp
