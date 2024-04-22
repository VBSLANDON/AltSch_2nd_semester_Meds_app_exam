from fastapi import FastAPI 

from pydantic import BaseModel

class Patients(BaseModel):
	id: int
	name: str
	age: int
	sex: str
	weight: float
	height: float
	phone: int


class PatientsCreate(BaseModel):
	name: str
	age: int
	sex: str
	weight: float
	height: float
	phone: int

    
patients: dict[int, Patients] = {
    0: Patients(
        id=0, name='patient 0', age=65, sex='Male', weight=156, height=75, phone='0810'
    ),
    1: Patients(
        id=1, name='patient 1', age=55, sex='female', weight=156, height=65, phone='0811'
    ),
    2: Patients(
        id=2, name='patient 2', age=65, sex='Male', weight=186, height=75, phone='0812'
    ),
}