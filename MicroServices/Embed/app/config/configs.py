from pydantic import BaseModel



class Config(BaseModel):
    API_V1_PREFIX: str = "/embed/api/v1"
    PROJECT_DESC: str = "Create Embeddings"
    PROJECT_TITLE: str = "Embedding Services"
    ORIGINS:list = ["*"]

settings = Config()
