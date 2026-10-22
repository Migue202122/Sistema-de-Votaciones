from pydantic import BaseModel


class VoteCreate(BaseModel):

    voter_id: int

    candidate_id: int