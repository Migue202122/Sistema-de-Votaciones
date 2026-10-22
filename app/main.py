from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.models.voter import Voter
from app.models.candidate import Candidate
from app.models.vote import Vote

from app.routers import voters
from app.routers import candidates
from app.routers import votes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(voters.router)
app.include_router(candidates.router)
app.include_router(votes.router)

@app.get("/")
def home():
    return {
        "message": "Sistema de Votaciones"
    }