from fastapi import FastAPI 
from pydantic import BaseModel
from schema.patient import Patients, patients
from typing import Union
from pydantic import BaseModel

doctors={}

class Doctors(BaseModel):
    name: str
    specialization:str
    phone: str
    is_available: Union[bool, None] = None

class DoctorsCreateEdit(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: Union[bool, None] = None

class DoctorsCreate(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: Union[bool, None] = None

doctors: dict[int, Doctors] = {
    0: Doctors(id=0, name='Dr. Landon Miles', specialization='Neurosurgeon', phone='08012309867', is_available=False),
    1: Doctors(id=1, name='Dr. Adufe Oyin', specialization='SCi-Tech', phone='07012359076'),
    2: Doctors(id=2, name='Dr. Steph Landon', specialization='Gynaecology', phone='07056489112')
}    
   