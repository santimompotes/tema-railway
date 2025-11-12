from unittest import result
from fastapi import APIRouter, Depends, HTTPException, logger, status
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.router.dependencies import get_current_user
from app.schemas.usuarios import CrearUsuario, EditarPass, EditarUsuario, RetornoUsuario
from core.database import get_db
from app.crud import usuarios as crud_users


def update_pdf_url(db: Session, cod: int ,url : str, file) -> bool:
    try:
        query = text(f"""UPDATE programas_formacion SET url_pdf = : url_pdf
                        WHERE cod_programa =: codigo """)
        db.execute(query ,{"url_pdf":url, "codigo": cod})
        db.commit()
        return True 
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error al actualizar el programa: {e}")
        raise Exception("Error de base de datos al actualizar el programa")

def get_programa_by_code(db:Session, cod:int):
    try:
        query = text(f"""SELECT * FROM prgramas_formacion
                        WHERE cod_programa =: codigo """)
        db.execute(query ,{"codigo": cod}).mappings().first()
        return result 
    except SQLAlchemyError as e:
        logger.error(f"Error al consultar el programa: {e}")
        raise Exception("Error de base de datos al consultar el programa")