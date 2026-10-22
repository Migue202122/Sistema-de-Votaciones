from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_candidate(
    candidate: CandidateCreate,
    db: Session = Depends(get_db)
):

    new_candidate = Candidate(
        name=candidate.name,
        party=candidate.party
    )

    db.add(new_candidate)

    db.commit()

    db.refresh(new_candidate)

    return new_candidate


@router.get("/")
def get_candidates(
    db: Session = Depends(get_db)
):

    return db.query(Candidate).all()
