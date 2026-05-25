from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes.predict import router as predict_router
from app.routes.pdf import router as pdf_router
from app.routes.report import router as report_router
from app.routes.chat import router as chat_router
from app.routes.gradcam import router as gradcam_router
from app.routes.cleanup import router as cleanup_router

#----FASTAPI APP----#

app = FastAPI(
    title="Brain Tumor MRI Classification API",
    description=("Explainable Vision-Language AI System "
                "for Brain Tumor Analysis"),
    version="1.0.0",
)

app.mount(
    "/static",
    StaticFiles(
        directory="ml/experiments"
    ),
    name="static",
)

#----CORS Configuration----#
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#----Health Check Endpoint----#

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "CereboVision API",
    }
            
app.include_router(pdf_router)
app.include_router(predict_router)
app.include_router(report_router)
app.include_router(chat_router)
app.include_router(gradcam_router)
app.include_router(cleanup_router)
