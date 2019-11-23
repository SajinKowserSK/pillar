from pymongo import MongoClient
from datetime import datetime
client = MongoClient("mongodb+srv://shafinsiddique:<Ishafin98>@cluster0-zv1ff.mongodb.net/test?retryWrites=true&w=majority")
database = client.get_database("shaman")

class PatientDBHelper:
    def __init__(self):
        self.collection = database.patientData

    def getDataForPatient(self, patientName):
        """Get all the data for patient with 'patientName' """

        return self.collection.findOne({"name":patientName})

    def addNewPatient(self, name):
        """insert a new patient into the system. This is when the patient
        registers for the first time. Only their name is stored and their medical record
        is empty."""

        self.collection.insertOne({"name":name, "medicalRecord":[]})

    def addMedicalDataForPatient(self, patientName, medicalData):
        """append new medical data for the patient with patientName"""

        query = {"name":patientName}
        self.collection.find_one_and_update(query,
                                                 {"$push": {"date": datetime.now(),
                                                          "data": medicalData}})


p = PatientDBHelper()
