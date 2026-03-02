import serial #import the module serial to python

ser=serial.Serial()
#crearte an object ser to call serial afterwards
#it should be noted, that objects are not part of the LC course but oddly are needed

ser.baudrate=115200
"""baudrate is a common unit of measurement in pulses per second that determines
the speed of communication over a data channel.

The number here is the microBit rate."""


ser.port='COM5' #your microBit is plugged into a port - check which one

ser.open()
#Ask the operating system to open the port to your program. It works the same as previously with .csv files

#********************************************************************************

"""
Next set up an infinite loop to retriece the data when a newline \n is detected.
"""
while True:
    data=str(ser.readline()) #read the line of data, convert it to a string store in the data
    data=data.replace("b", "") #get rif og the b infront of the data
    data=data.replace("'", "") #get rid of the ' infront of and after the data
    data=data.replace(" ", "") #get rid of the spaces
    data=data.replace("\\r\\n", "") #get rid of the \r\n 
    print(data)
