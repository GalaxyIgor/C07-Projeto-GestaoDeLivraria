from pydantic import BaseModel, Field


class Autor(BaseModel):
    idAutor: int
    nomeAutor: str = Field(max_length=120)
    nacionalidadeAutor: str = Field(max_length=60)
