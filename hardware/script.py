from time import sleep
import requests
import serial
import polling
from pymongo import MongoClient
from datetime import datetime

client = MongoClient(
    "mongodb+srv://shafinsiddique:Ishafin98@cluster0-zv1ff.mongodb.net/test?retryWrites=true&w=majority")
database = client.get_database("shaman")
collection = database.dispense


def poll():
    result = collection.find({"dispense": "0"})
    return False if result == None else True


# Establish the connection on a specific port
ser = serial.Serial('/dev/tty.usbmodem14201', 9600)

while True:
    dispense_pill = poll()
    ser.write(dispense_pill)
    if (dispense_pill):
        collection.update_one({"dispense": "1"},  {"$set": {"dispense": "0"}}))
    print(dispense_pill)
    sleep(.1)
    # Delay for one tenth of a second
