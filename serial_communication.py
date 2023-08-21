import serial

try:
    # Open COM17 for sending and COM22 for receiving
    #This code block opens two serial ports: 'COM17' and 'COM22'. 
    # The baudrate parameter sets the communication speed to 9600 bits 
    # per second. 
    # Serial communication involves sending and receiving binary data between devices.
    com17 = serial.Serial('COM17', baudrate=9600)
    com22 = serial.Serial('COM22', baudrate=9600)
    
    # com17.open()
    
    # Send data from COM17
    print("writing")

    #These lines send data from the 'com17' and 'com22' serial ports. The write method sends binary data to the respective serial ports. In this case, 'Hello, world!' is sent from 'com17', and 'Hi' is sent from 'com22'.
    com17.write(b'Hello, world!')
    
    # Receive data on COM22
    print("reading")

    #This line reads data from the 'com22' serial port using the readline() method. It waits until a newline character ('\n') is received or the buffer is full, and then it returns the received data as bytes.
    received_data = com22.readline()  # Read up to 100 bytes
    print("Received:", received_data)

    # Close the ports
    com17.close()
    com22.close()

except Exception as e:
    print("An error occurred:", e)
