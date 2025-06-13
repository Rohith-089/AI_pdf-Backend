from config.dB import   pdf_collection
from bson import ObjectId
from typing import List, Optional
from schema.pdf import PDFBase, PDFOut

# Helper to convert MongoDB documents to dicts
def pdf_helper(pdf) -> dict:
    return {
        "id": str(pdf["_id"]),
        "filename": pdf["filename"],
        "content": pdf["content"],
        "summary": pdf["summary"]
    }

# Create a new PDF entry
async def add_pdf(pdf_data: PDFBase) -> PDFOut:
    pdf = await pdf_collection.insert_one(pdf_data.dict())
    new_pdf = await pdf_collection.find_one({"_id": pdf.inserted_id})
    return PDFOut(**pdf_helper(new_pdf))

# Get all PDFs
async def get_all_pdfs() -> List[PDFOut]:
    pdfs = []
    async for pdf in pdf_collection.find():
        pdfs.append(PDFOut(**pdf_helper(pdf)))
    return pdfs

# Get PDF by ID
async def get_pdf_by_id(pdf_id: str) -> Optional[PDFOut]:
    pdf = await pdf_collection.find_one({"_id": ObjectId(pdf_id)})
    if pdf:
        return PDFOut(**pdf_helper(pdf))
    return None
