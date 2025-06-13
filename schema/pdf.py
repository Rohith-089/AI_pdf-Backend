from pydantic import BaseModel
from typing import Optional

class PDFBase(BaseModel):
    filename: str
    content: str
    summary: str

class PDFOut(PDFBase):
    id: Optional[str]
