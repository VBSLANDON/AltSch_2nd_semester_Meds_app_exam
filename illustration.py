# You are building an API for a medical appointment application. 

# The application has the following entities:

# Patient: id, name, age, sex, weight, height, phone

# Doctors: id, name, specialization, phone, is_available (defaults to True)

# Appointment: id, patient, doctor, date

# Description

# The application is to facilitate appointment bookings between Patients and Doctors. A doctor can only have one appointment scheduled with a patient at a time, so if a patient needs to book an appointment and no doctor is available, your API should respond with the proper response and status code

# The API should provide the following endpoints:

# CRUD endpoints for Patients
# CRUD endpoints for Doctors
# Create an appointment. Only patients can create an appointment. When a patient tries to create an appointment, the first available doctor is assigned to the Appointment. If no doctors are available, return the appropriate response and status code to the user.
# Complete an appointment. Doing this will make the Doctor available again and other patients can book the doctor.
# Cancel an appointment before it is completed, making the doctor free again.
# Set availability status. This is for the Doctors, allowing them to set their status to unavailable to prevent them from being booked.