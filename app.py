import json
from fastapi import FastAPI
from models import TaxForm, PromptEnum
from utils import io_generator, content_extracter, form_uploader, get_prompt
import prompts

app = FastAPI()

@app.get('/')
def read_root():
    return {
        "message": "Server is running..."
    }

@app.post('/analyze/{form_type}')
async def pdf_analyzer(tax_form: TaxForm, form_type: PromptEnum) -> dict:
    
    form_io = await io_generator(tax_form.pdf_url)
    uploaded_form = await form_uploader(form_io)
    prompt_text = get_prompt(form_type.value)
    unformatted_extracted_content = await content_extracter(uploaded_form, prompt_text)
    
    return {
        "inputs": {
            "pdf_url": tax_form.pdf_url,
            "form_type": form_type.value
        },
        "output": json.loads(unformatted_extracted_content.text)
    }
    