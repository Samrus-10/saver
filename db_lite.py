from fastapi import Depends
from typing import Annotated
from sqlmodel import create_engine, Session, SQLModel


sqlite_file_name = 'db/database.bd'
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread" : False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]