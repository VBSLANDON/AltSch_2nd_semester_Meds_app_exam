from fastapi import APIRouter

from schema.doctor import DoctorsCreate, DoctorsCreateEdit, Doctors, doctors
from services.doctor import DoctorService

doctor_router = APIRouter()

@doctor_router.get('/', status_code=200)
def get_doctors():
    data = DoctorService.parse_doctors(doctor_data=doctors)
    return {'message': 'Successfully Get', 'data': data}


@doctor_router.get('/{doctor_id}', status_code=200)
def get_doctor_by_id(doctor_id: int):
    data = DoctorService.get_doctors_by_id(doctor_id)
    return {'message': 'Successfully Get', 'data': data}


@doctor_router.post('/', status_code=201)
def create_doctor(payload: DoctorsCreate):
    data = DoctorService.create_doctor(payload)
    return {'message': 'Doctor Created', 'data': data}


@doctor_router.put('/{doctor_id}', status_code=200)
def edit_doctor(doctor_id: int, payload: DoctorsCreateEdit):
    data = DoctorService.edit_doctor(doctor_id, payload)
    return {'message': 'Your doctor info updated successfully', 'data': data}


@doctor_router.delete('/{doctor_id}', status_code=200)
def delete_doctor(doctor_id: int):
    DoctorService.delete_doctor(doctor_id)
    return {'message': 'Doctor Info Deleted Successfully'}


@doctor_router.put('/set_availability/{doctor_id}', status_code=200)
def set_availability(doctor_id: int):
    data = DoctorService.set_availability_status(doctor_id)
    return {'message': 'Doctor Availability Updated Successfully', 'data': data}