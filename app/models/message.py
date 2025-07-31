from pydantic import BaseModel
from datetime import datetime

class RequestMessage(BaseModel):
    timestamp: datetime
    request: str


class ResponseMessage(BaseModel):
    reply: str
    timestamp: datetime