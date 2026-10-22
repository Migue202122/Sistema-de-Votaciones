from pydantic import BaseModel


class CandidateCreate(BaseModel):

    name: str

    party: str | None = None