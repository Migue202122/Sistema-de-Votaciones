from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models.vote import Vote
from app.models.voter import Voter
from app.models.candidate import Candidate

from app.schemas.vote import VoteCreate

from app.utils.chart import generate_chart

router = APIRouter(
    prefix="/votes",
    tags=["Votes"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_vote(
    vote: VoteCreate,
    db: Session = Depends(get_db)
):

    voter = db.query(Voter)\
        .filter(Voter.id == vote.voter_id)\
        .first()

    if not voter:
        raise HTTPException(
            status_code=404,
            detail="Votante no encontrado"
        )

    if voter.has_voted:
        raise HTTPException(
            status_code=400,
            detail="Este votante ya voto"
        )

    candidate = db.query(Candidate)\
        .filter(Candidate.id == vote.candidate_id)\
        .first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidato no encontrado"
        )

    new_vote = Vote(
        voter_id=vote.voter_id,
        candidate_id=vote.candidate_id
    )

    db.add(new_vote)

    voter.has_voted = True

    candidate.votes += 1

    db.commit()

    db.refresh(new_vote)

    return {
        "message": "Voto registrado correctamente"
    }


@router.get("/")
def get_votes(
    db: Session = Depends(get_db)
):

    return db.query(Vote).all()

@router.get("/statistics")
def get_statistics(
    db: Session = Depends(get_db)
):

    candidates = db.query(Candidate).all()

    total_votes = sum(
        candidate.votes
        for candidate in candidates
    )

    results = []

    for candidate in candidates:

        percentage = 0

        if total_votes > 0:
            percentage = round(
                (candidate.votes / total_votes) * 100,
                2
            )

        results.append({
            "candidate": candidate.name,
            "votes": candidate.votes,
            "percentage": percentage
        })

    return {
        "total_votes": total_votes,
        "total_voters_voted": db.query(Voter)
            .filter(Voter.has_voted == True)
            .count(),
        "results": results
    }

@router.get("/chart")
def create_chart(
    db: Session = Depends(get_db)
):

    candidates = db.query(
        Candidate
    ).all()

    generate_chart(candidates)

    return {
        "message": "Grafica generada correctamente"
    }