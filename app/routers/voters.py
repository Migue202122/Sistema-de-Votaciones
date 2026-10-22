from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.voter import Voter
from app.schemas.voter import VoterCreate

router = APIRouter(
    prefix="/voters",
    tags=["Voters"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_voter(
    voter: VoterCreate,
    db: Session = Depends(get_db)
):

    existing_voter = db.query(Voter)\
        .filter(Voter.email == voter.email)\
        .first()

    if existing_voter:
        raise HTTPException(
            status_code=400,
            detail="El email ya está registrado"
        )

    new_voter = Voter(
        name=voter.name,
        email=voter.email
    )

    db.add(new_voter)

    db.commit()

    db.refresh(new_voter)

    return new_voter

@router.delete("/{id}")
def delete_voter(
    id: int,
    db: Session = Depends(get_db)
):

    voter = db.query(Voter)\
        .filter(Voter.id == id)\
        .first()

    if not voter:
        raise HTTPException(
            status_code=404,
            detail="Votante no encontrado"
        )

    db.delete(voter)

    db.commit()

    return {
        "message": "Votante eliminado correctamente"
    }