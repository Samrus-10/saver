from sqlmodel import Field, SQLModel
from typing import Dict, Any
from pydantic import BaseModel

class Payload(BaseModel):
    url: str | None
    method: str | None
    request: Dict[str, Any] 
    response: Dict[str, Any] 


class Data(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    url: str | None = Field(default=None)
    method: str | None = Field(default=None)
    request: str | None =  Field(default=None)
    response: str | None =  Field(default=None)