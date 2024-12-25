from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import FastAPI
from .routes import router

router = APIRouter()

class TrackParams(BaseModel):
    length: float
    width: float

@router.post("/generate-track")
async def generate_track(params: TrackParams):
    return {"message": f"Track generated with length {params.length} and width {params.width}"}


app = FastAPI()
app.include_router(router)
