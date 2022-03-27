import serial


def connectArduino():
    print("connect arduino")
    ser = serial.Serial()
    print("serial object created")
    ser.baudrate = 9600
    print("baudrate set")
    ser.port = 'COM7'
    print("port set")
    ser.open()
    print("serial port opened")
    while True:
        if ser.in_waiting:
            line = ser.readline()
            print(line.decode("utf-8").rsplit("\r\n")[0])
            
            
            
connectArduino()

