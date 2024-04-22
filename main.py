from fastapi import FastAPI

from routers.patient import patient_router
from routers.doctor import doctor_router
from routers.appointment import appointment_router

app = FastAPI()

app.include_router(router=patient_router, prefix='/patients', tags=['patients'])
app.include_router(router=doctor_router, prefix='/doctors', tags=['doctors'])
app.include_router(router=appointment_router,prefix='/appointments', tags=['appointments'])

@app.get('/')
def home():
    return 'Welcome to Medical Appointment'

