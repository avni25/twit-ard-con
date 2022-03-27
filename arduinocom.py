import serial


def readPort(PORT):
    print("connect arduino")
    ser = serial.Serial()
    print("serial object created")
    ser.baudrate = 9600
    print("baudrate set")
    ser.port = PORT
    print("port set")
    ser.open()
    print("serial port opened")
    res =""
    while True:
        if ser.in_waiting:
            line = ser.readline()
            print(line.decode("utf-8").rsplit("\r\n")[0])
            res = line.decode("utf-8").rsplit("\r\n")[0]
            return res
            
            
