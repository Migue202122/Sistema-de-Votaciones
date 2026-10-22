from pydantic import BaseModel
from pydantic import EmailStr


class VoterCreate(BaseModel):

    name: str
    email: EmailStr