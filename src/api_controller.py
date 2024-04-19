"""Patient API Controller"""

from flask import Flask, request, jsonify
from patient_db import PatientDB
from config import ROOM_NUMBERS,WARD_NUMBERS,GENDERS


class PatientAPIController:
    def __init__(self):
        self.app = Flask(__name__)
        self.patient_db = PatientDB()
        self.setup_routes()
        self.run()

    def setup_routes(self):
        """
        Sets up the routes for the API endpoints.
        """
        self.app.route("/patients", methods=["GET"])(self.get_patients)
        self.app.route("/patients/<patient_id>", methods=["GET"])(self.get_patient)
        self.app.route("/patients", methods=["POST"])(self.create_patient)
        self.app.route("/patient/<patient_id>", methods=["PUT"])(self.update_patient)
        self.app.route("/patient/<patient_id>", methods=["DELETE"])(self.delete_patient)

    """
    TODO:
    Implement the following methods,
    use the self.patient_db object to interact with the database.

    Every method in this class should return a JSON response with status code
    Status code should be 200 if the operation was successful,
    Status code should be 400 if there was a client error,
    """

    def create_patient(self):
        try:
            data = request.json  # Get JSON data from request
            if not data:
                return jsonify({"error": "No data provided"}), 400

            if data["patient_gender"] not in GENDERS:
                return jsonify({"error": "Gender is not valid"}), 400

            if data["patient_room"] not in ROOM_NUMBERS:
                return jsonify({"error": "Room is not valid"}), 400
            
            if data["patient_ward"] not in WARD_NUMBERS:
                return jsonify({"error": "Room is not valid"}), 400
        
            self.patient_db.insert_patient(data)

            return jsonify({"message": "Patient created successfully"}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def get_patients(self):
        patients = self.patient_db.select_all_patients()
        if patients is not None:
            return patients
        
        return  {[]}

    def get_patient(self, patient_id):
        patient = self.patient_db.select_patient(patient_id)
        if patient is None:
            return jsonify({"error": "No patient with this id"}), 400

        return patient, 200

    def update_patient(self, patient_id):   
        try:
            data = request.json  # Get JSON data from request
            if not data:
                return jsonify({"error": "No data provided"}), 400

            if data["patient_gender"] not in GENDERS:
                return jsonify({"error": "Gender is not valid"}), 400

            if data["patient_room"] not in ROOM_NUMBERS:
                return jsonify({"error": "Room is not valid"}), 400
            
            if data["patient_ward"] not in WARD_NUMBERS:
                return jsonify({"error": "Room is not valid"}), 400
        
            self.patient_db.update_patient(patient_id,data)

            return jsonify({"message": "Patient Updated successfully"}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def delete_patient(self, patient_id):
        deletation = self.patient_db.delete_patient(patient_id)
        if deletation is None:
            return jsonify({"error": "Could not delete pationt or no patient with this id"}), 400
        
        return jsonify({"message": "Patient Deleted successfully"}), 200

    def run(self):
        """
        Runs the Flask application.
        """
        self.app.run()


PatientAPIController()
