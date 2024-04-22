from fastapi import HTTPException
from schema.doctor import doctors
from schema.appointment import appointments, AppointmentsCreateEdit
from schema.patient import patients
from services import patient


class AppointmentHelpers:

    @staticmethod
    def appoint_doctor_to_patient():
        for doctor_id, doctor in doctors.items():
            if doctor.is_available == True:
                doctor.is_available = False
                return doctors[doctor_id]
        raise HTTPException(
            detail='All doctors are currently busy', status_code=404)

    @staticmethod
    def get_appointment_by_id(appointment_id: int):
        appointment = appointments.get(appointment_id)
        if not appointment:
            raise HTTPException(
                detail='Appointment not schedule', status_code=404)
        return appointment

    @staticmethod
    def set_doctor_availability_true(appointment):
        for doc, doctor in doctors.items():
            if doctor == appointment.doctor:
                doctor.is_available = True
        return appointment