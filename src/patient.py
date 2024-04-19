"""
TODO: Implement the Patient class.
Please import and use the config and db config variables.

The attributes for this class should be the same as the columns in the PATIENTS_TABLE.

The Object Arguments should only be name , gender and age.
Rest of the attributes should be set within the class.

-> for id use uuid4 to generate a unique id for each patient.
-> for checkin and checkout use the current date and time.

There should be a method to update the patient's room and ward. validation should be used.(config is given)

Validation should be done for all of the variables in config and db_config.

There should be a method to commit that patient to the database using the api_controller.
"""

import uuid
from datetime import datetime, date
from config import GENDERS,WARD_NUMBERS,ROOM_NUMBERS


class Patient:
    patient_id = ""
    patient_name = ""
    patient_age = ""
    patient_gender = ""
    patient_checkin = ""
    patient_checkout = ""
    patient_ward = ""
    patient_room = ""

    def __init__(self, Name, Gender, Age):
        self.patient_name = Name
        
        if self.patient_gender not in GENDERS:
            raise Exception("Gender not a valid gender")
        
        self.patient_gender = Gender
        self.patient_age = Age

        self.patient_id = uuid.uuid4()
        
    def checkin(self):
        self.patient_checkin = datetime.now()

    def checkout(self):
        self.patient_checkout = datetime.now()

    def set_room(self,room:int):
        if room not in ROOM_NUMBERS:
            raise Exception("Room number not valid")
        
        self.patient_room = room
            
    def set_ward(self,ward):
        if ward not in WARD_NUMBERS:
            raise Exception("Room number not valid")
        
        self.patient_ward = ward