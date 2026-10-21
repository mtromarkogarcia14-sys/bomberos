from fastapi import FastAPI
from app.database import Base, engine
from app.routes.municipalities import router as municipalities_router
from app.routes.programs import router as programs_router
from app.routes.cases import router as cases_router
from app.routes.compliance import router as compliance_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Jalisco Municipal Fire Compliance Agent")

app.include_router(municipalities_router)
app.include_router(programs_router)
app.include_router(cases_router)
app.include_router(compliance_router)

@app.get("/health")
def health():
    return {"status": "ok"}