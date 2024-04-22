from fastapi import HTTPException

from schema import appointment
from schema.appointment import Appointments, AppointmentsCreateEdit, AppointmentsStatus, appointments
from schema.doctor import Doctors, doctors
from schema.patient import patients
from utilis.appointment import AppointmentHelpers


class AppointmentService:

    @staticmethod
    def parse_appointments(appointment_data):
        data = []
        for appointment in appointment_data:
            data.append(appointments[appointment])
        return data

    @staticmethod
    def get_appointment_by_id(appointment_id: int):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
        return appointment

    @staticmethod
    def create_appointment(payload: AppointmentsCreateEdit):
        id = len(appointments)
        patient = patients.get(payload.patient_id)
        if not patient:
            raise HTTPException(detail='Patient not in list', status_code=404)

        # Check if patient has pending appointment

        for key, appointment in appointments.items():
            if patient == appointment.patient and appointment.status == AppointmentsStatus.PENDING:
                raise HTTPException(
                    detail='Patient has pending schedule appointment. Please complete pending schedule appointment', status_code=200)

        doctor: Doctors = AppointmentHelpers.appoint_doctor_to_patient()

        appointment = Appointments(
            id=id,
            patient=patient,
            doctor=doctor,
            date=payload.date
        )
        appointments[id] = appointment
        return appointment

    @staticmethod
    def edit_appointment(appointment_id: int, payload: AppointmentsCreateEdit):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)

        appointment.patient = patients.get(payload.patient_id)
        if appointment.patient is None:
            raise HTTPException(
                detail='Patient not in list.', status_code=404
            )
        appointment.date = payload.date
        return appointment

    @staticmethod
    def delete_appointment(appointment_id: int):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)

        AppointmentHelpers.set_doctor_availability_true(appointment)

        del appointments[appointment_id]

    @staticmethod
    def complete_appointment(appointment_id: int):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
        appointment.status = AppointmentsStatus.COMPLETED

        AppointmentHelpers.set_doctor_availability_true(appointment)

        return appointment