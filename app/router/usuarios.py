from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.router.dependencies import get_current_user
from app.schemas.usuarios import CrearUsuario, EditarPass, EditarUsuario, RetornoUsuario
from core.database import get_db
from app.crud import usuarios as crud_users

router = APIRouter()

@router.post("/registrar", status_code=status.HTTP_201_CREATED)
def create_user(
    user: CrearUsuario,
    db: Session = Depends(get_db),
    user_token: RetornoUsuario = Depends(get_current_user)
    ):
    try:
        if user_token != 1:
            raise HTTPException(status_code=401, detail="No tienes permiso para crear usuarios")
        crear = crud_users.create_user(db, user)
        if crear:
            return {"message": "Usuario creado correctamente"}
        else:
            return {"message": "Usuario no se hacreado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/obtener_por_id/{id_usuario}", response_model=RetornoUsuario)
def get_user_by_id(id_usuario: int, db: Session = Depends(get_db)):
    try:
        user = crud_users.get_user_by_id(db, id_usuario)
        if user is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user 
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {e}")


@router.get("/obtener_por_correo/{correo}", response_model=RetornoUsuario)
def get_user_by_email(correo: str, db: Session = Depends(get_db)):
    try:
        user = crud_users.get_user_by_email(db, correo)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
        return user 
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {e}")
    

@router.delete("/eliminar_por_id/{id_usuario}", status_code=status.HTTP_200_OK)
def delete_by_id(id_usuario: int, db: Session = Depends(get_db)):
    try:
        crud_users.delete_by_id(db, id_usuario)
        return {"message": "Usuario eliminado correctamente"}
    except HTTPException as e:
        # Reenviamos las excepciones controladas (404 o 500)
        raise e
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {e}")

@router.put("/editar/{user_id}")
def update_user(user_id: int, user: EditarUsuario, db: Session = Depends(get_db)):
    try:
        success = crud_users.update_user(db, user_id, user)
        if not success:
            raise HTTPException(status_code=400, detail="No se pudo actualizar el usuario")
        return {"message": "Usuario actualizado correctamente"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/editar.contrasenia")
def update_password(user: EditarPass, db: Session = Depends(get_db)):
    try:
        verificar = crud_users.verify_user_pass(db, user)
        if not verificar:
            raise HTTPException(status_code=400, detail="La contraseña actual no es igual a la enviada")

        success = crud_users.update_password(db, user)
        if not success:
            raise HTTPException(status_code=400, detail="No se pudo actualizar la contraseña")
        return {"message": "Contraseña actualizada correctamente"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))