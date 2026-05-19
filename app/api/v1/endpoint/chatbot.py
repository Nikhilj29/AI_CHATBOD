from fastapi import APIRouter, File,UploadFile
from pypdf import PdfReader
import io
import re
router = APIRouter()

@router.post("/")
async def postchat(query:str,file:UploadFile = File(...)):
    print(file,"file")
    print(query,"query")
    
    file_bytes = await file.read()
    file_stream  = io.BytesIO(file_bytes)
    document_read = PdfReader(file_stream)
    print(document_read,"document read")
    text = ""
    for i in document_read.pages:
        extracting = i.extract_text()
        text =  text + extracting
    
    print(text,"text")
    
    extracting_text_array = re.split(r'[.|:]', text)
    print(extracting_text_array,"array")
    return "GOT STRING"