from datetime import date
from enum import Enum
from pydantic import BaseModel

from schema.doctor import Doctors, doctors
from schema.patient import Patients, patients


class AppointmentsStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"


class Appointments(BaseModel):
    id: int
    patient: Patients
    doctor: Doctors
    date: date
    status: AppointmentsStatus = AppointmentsStatus.PENDING


class AppointmentsCreateEdit(BaseModel):
    patient_id: int
    date: date


appointments: dict[int, Appointments] = {
    0: Appointments(
        id=0, patient=patients[0], doctor=doctors[0], date=date(2024, 4, 22)
    )
}