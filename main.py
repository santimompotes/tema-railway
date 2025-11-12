from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.router import auth
from app.router import auth
from fastapi.middleware.cors import CORSMiddleware
from app.router import usuarios

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"),name="static")

# Incluir en el objeto app los routers
app.include_router(usuarios.router, prefix="/usuario", tags=["Servicios Usuarios"])
app.include_router(auth.router, prefix="/access", tags=["autenticacion"])
app.include_router(auth.router, prefix="/access", tags=["autenticacion"])
app.include_router(auth.router, prefix="/access", tags=["autenticacion"])

# Configuración de CORS para permitir todas las solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permitir estos métodos HTTP  
    allow_headers=["*"],  # Permitir cualquier encabezado en las solicitudes
)

@app.get("/")
def read_root():
    return {
                "message": "ok",
                "autor": "ADSO 2925888"
            }