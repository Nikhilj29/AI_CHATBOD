from fastapi import APIRouter, File,UploadFile
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import io
import nltk
import numpy as np
import faiss

router = APIRouter()


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

nltk.download('punkt', quiet=True)
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
    
    extracted_array = nltk.sent_tokenize(text)
    print(extracted_array,"extracted array")
    
    embedding = model.encode(extracted_array)
    
    db_vector = np.array(embedding,dtype=np.float32)
    dimention = db_vector.shape[1]
    
    index = faiss.IndexFlatL2(dimention)
    
    index.add(db_vector)    
    query_array = [query]
    query_embediing = model.encode(query_array)
    
    query_vector = np.array(query_embediing,dtype=np.float32)
    
    distance_of_sol,index_of_sol = index.search(query_vector,k=1)
    
    print(distance_of_sol,index_of_sol,"result")    
    
    best_match_index = index_of_sol[0][0]
    
    print(best_match_index,"best match index")
    
    print(extracted_array[best_match_index],"SOlution")
    
    return extracted_array[best_match_index]