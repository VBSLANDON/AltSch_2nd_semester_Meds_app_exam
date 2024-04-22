from fastapi import HTTPException
from schema.doctor import DoctorsCreate, Doctors, DoctorsCreateEdit, doctors
from schema.patient import patients

class DoctorService:

    @staticmethod
    def parse_doctors(doctor_data):
        data = []
        for doctor in doctor_data:
            data.append(doctors[doctor])
        return data

    @staticmethod
    def get_doctors_by_id(doctor_id: int):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(
                detail='Doctor not found.', status_code=404)
        return doctor

    @staticmethod
    def create_doctor(payload: DoctorsCreate):
        id = len(doctors)
        doctor = Doctors(
            id=id,
            **payload.model_dump()
        )
        doctors[id] = doctor
        return doctor

    @staticmethod
    def edit_doctor(doctor_id: int, payload: DoctorsCreateEdit):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(
                detail='Doctor not found.', status_code=404)

        if payload.name != None:
            doctor.name = payload.name
        if payload.specialization != None:
            doctor.specialization = payload.specialization
        if payload.phone != None:
            doctor.phone = payload.phone
        return doctor

    @staticmethod
    def delete_doctor(doctor_id: int):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(
                detail='Doctor not found.', status_code=404)
        del doctors[doctor_id]

    @staticmethod
    def set_availability_status(doctor_id: int):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(
                detail='Doctor not found.', status_code=404)

        if doctor.is_available == True:
            doctor.is_available = False
        else:
            doctor.is_available = True

        return doctor