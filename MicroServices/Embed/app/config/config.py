from pydantic import BaseModel



class Config(BaseModel):
    API_V1_PREFIX: str = "/embed/api/v1"
    PROJECT_DESC: str = "Create Embedding"
    PROJECT_TITLE: str = "Document Embedding Services"
    ORIGINS:list = ["*"]

settings = Config()
