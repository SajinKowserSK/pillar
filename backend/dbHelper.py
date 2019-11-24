from pymongo import MongoClient
from datetime import datetime
import summarizer
client = MongoClient("mongodb+srv://shafinsiddique:Ishafin98@cluster0-zv1ff.mongodb.net/test?retryWrites=true&w=majority")
database = client.get_database("shaman")

class PatientDBHelper:
    def __init__(self):
        self.collection = database.patientData

    def getAllPatients(self):
        documents = []

        for docs in self.collection.find({}):
            del docs['_id']
            documents.append(docs)

        return documents


    def getDataForPatient(self, patientName):
        """Get all the data for patient with 'patientName' """

        return self.collection.find_one({"name":patientName})

    def addNewPatient(self, name, age, sex, height, weight, bloodtype,  symptoms,
                      curr_sentiment, numberOfVisits):

        """insert a new patient into the system. This is when the patient
        registers for the first time. Only their name is stored and their medical record
        is empty."""

        self.collection.insert_one({"name":name, "medicalRecord":[],
                                    "age":age, "sex":sex,"height":height,
                                    "weight":weight,
                                    "blood_type":bloodtype,"prescription":[],
                                    "number_of_visits":numberOfVisits,
                                    "curr_symptoms":symptoms,
                                    "curr_sentiment":curr_sentiment})


        print("{} added to the patient database.".format(name))

    def addMedicalDataForPatient(self, patientName, medicalData):
        """append new medical data for the patient with patientName"""

        query = {"name":patientName}
        summary = summarizer.summarize(medicalData, True)
        self.collection.update_one(query,{"$push": {"medicalRecord": {"date":datetime.now(),"data":summary}}})
        self.collection.update_one(query,{"$inc":{"number_of_visits":1}})
        self.collection.update_one(query, {"$set":{"curr_sentiment":summary['sentiment']}})
        print("Medical Record updated for patient {}".format(patientName))


if __name__ == "__main__":
    p = PatientDBHelper()
