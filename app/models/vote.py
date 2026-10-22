from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.database import Base


class Vote(Base):

    __tablename__ = "votes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    voter_id = Column(
        Integer,
        ForeignKey("voters.id")
    )

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id")
    )
