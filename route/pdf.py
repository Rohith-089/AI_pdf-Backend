from fastapi import APIRouter, HTTPException
from typing import List
from models.pdf import add_pdf, get_all_pdfs, get_pdf_by_id
from schema.pdf import PDFBase, PDFOut

router = APIRouter(
    prefix="/pdfs",
    tags=["PDFs"]
)

@router.post("/", response_model=PDFOut, status_code=201)
async def create_pdf(pdf_data: PDFBase):
    new_pdf = await add_pdf(pdf_data)
    return new_pdf

@router.get("/", response_model=List[PDFOut])
async def read_pdfs():
    pdfs = await get_all_pdfs()
    return pdfs

@router.get("/{pdf_id}", response_model=PDFOut)
async def read_pdf(pdf_id: str):
    pdf = await get_pdf_by_id(pdf_id)
    if pdf:
        return pdf
    raise HTTPException(status_code=404, detail="PDF not found")
