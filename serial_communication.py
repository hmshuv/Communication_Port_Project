import serial

try:
    # Open COM17 for sending and COM22 for receiving
    com17 = serial.Serial('COM17', baudrate=9600)
    com22 = serial.Serial('COM22', baudrate=9600)
    
    # com17.open()
    
    # Send data from COM17
    print("writing")
    com17.write(b'Hello, world!')
   
    # Receive data on COM22
    print("reading")
    received_data = com22.readline()  # Read up to 100 bytes
    print("Received:", received_data)

    # Close the ports
    com17.close()
    com22.close()

except Exception as e:
    print("An error occurred:", e)
