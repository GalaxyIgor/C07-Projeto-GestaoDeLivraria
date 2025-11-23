from pydantic import BaseModel, Field


class Editora(BaseModel):
    idEditora: int
    nomeEditora: str = Field(max_length=100) 
    cnpjEditora: str = Field(max_length=20)
    localEditora: str = Field(max_length=45) # CORRIGIDO: max_lenght -> max_length