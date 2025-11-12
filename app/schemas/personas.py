from typing import Optional
from datetime import date
from pydantic import BaseModel, EmailStr, Field

class PersonaBase(BaseModel):
    nombre_completo: str = Field(min_length=3, max_length=80)
    tipo_documento: str = Field(min_length=3, max_length=3)
    cedula: str = Field(min_length=8, max_length=12)
    fecha_expedicion: str = Field(min_length=11, max_length=11)
    lugar_expedicion: str = Field(min_length=10, max_length=40)
    fecha_nacimiento: date = Field(...)
    departamento_nacimiento: str = Field(min_length=4, max_length=21)
    municipio_nacimiento: str = Field(min_length=3, max_length=27)
    genero: str = Field(min_length=8, max_length=9)
    sexo: str = Field(min_length=4, max_length=6)

    tipo_poblacion: str = Field(min_length=0, max_length=0)
    lgbti: str = Field(min_length=0, max_length=0)
    discapacidad: str = Field(min_length=0, max_length=0)
    estado_civil: str = Field(min_length=0, max_length=0)
    escolaridad: str = Field(min_length=0, max_length=0)
    departamento_domicilio: str = Field(min_length=0, max_length=0)
    municipio_domicilio: str = Field(min_length=0, max_length=0)
    direccion: str = Field(min_length=0, max_length=0)
    barrio: str = Field(min_length=0, max_length=0)
    estrato: str = Field(min_length=0, max_length=0)
    telefono: str = Field(min_length=0, max_length=0)
    celular: str = Field(min_length=0, max_length=0)
    email: str = EmailStr
    usuario: str = Field(min_length=0, max_length=0)
    encuesta: str = Field(min_length=0, max_length=0)

class CrearPersona(PersonaBase):
    estado: bool = True


