from time import sleep
import requests
import serial


URL = 'http://localhost:5000/summarize/'


def test():
    text = "Mrs. Smith states that on Sunday evening (7/14/03) about 20 minutes after sitting down to work at her computer, she developed blurred vision, which she describes as the words on the computer looking fuzzy and seeming to run into each other. When she looked up at the clock on the wall, she had a hard time making out the numbers. At the same time, she also noted a strange sensation in her right eyelid."
    data = {'text': text}
    r = requests.post(url=URL, data=data)
    print(r)
    return r


# Establish the connection on a specific port
ser = serial.Serial('/dev/tty.usbmodem14201', 9600)
counter = 32  # Below 32 everything in ASCII is gibberish
while True:
    counter += 1
    # Convert the decimal number to ASCII then send it to the Arduino
    ser.write(1)
    print(ser.readline())  # Read the newest output from the Arduino
    sleep(.1)  # Delay for one tenth of a second
    if counter == 255:
        counter = 32

# test()
