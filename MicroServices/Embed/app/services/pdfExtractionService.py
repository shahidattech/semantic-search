import os
import fitz  # PyMuPDF
import logging

def extract_text_from_pdf(pdf_path):
   try: 
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text
   except IOError as Err:
      logging.error("====IOError Error in extract_text_from_pdf" + str(Err))
      raise Err
   except Exception as Err:
      logging.error("====Error in extract_text_from_pdf" + str(Err))
      raise Err