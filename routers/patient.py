from fastapi import APIRouter, Response, Depends
from pydantic import BaseModel
from schema.patient import Patients, PatientsCreate, patients
from services.patient import PatientService

patient_router = APIRouter()

@patient_router.get('/', status_code=200)
def get_patients():
    data = PatientService.parse_patients(patient_data=patients)
    return{'message': 'successful', 'data': data}

@patient_router.get('/{patient_id}', status_code=200)
def get_patient_by_id(patient_id: int):
    data = PatientService.get_patient_by_id(patient_id)
    return{'message': 'successful', 'data': data}

@patient_router.post('/', status_code=201)
def create_patient(payload: PatientsCreate):
    data = PatientService.create_patient(payload)
    return {'message': 'Created', 'data': data}
