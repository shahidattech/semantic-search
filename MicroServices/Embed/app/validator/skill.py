from pydantic import BaseModel, Field
import json
from typing import Optional

class Topic(BaseModel):
    topic_name: str = Field(min_length=3, max_length=12)
    plain_text: Optional[str] = "" or None