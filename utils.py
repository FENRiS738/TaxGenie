import os
import io
from dotenv import load_dotenv
import httpx
from google import genai
from google.genai import types
import prompts

load_dotenv()
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=GENAI_API_KEY)

async def io_generator(pdf_url):
    async with httpx.AsyncClient(follow_redirects=True) as http_client:
            form_response = await http_client.get(pdf_url)
            form_response.raise_for_status()
            
            
            content = form_response.content
            if not content.startswith(b'%PDF'):
                raise ValueError("The downloaded file does not appear to be a valid PDF")
            
            form_io = io.BytesIO(content)
            form_io.seek(0)
            return form_io



async def form_uploader(form_io):
    uploaded_form = await client.aio.files.upload(
        file=form_io,
        config=types.UploadFileConfig(
            mime_type='application/pdf'
        )
    )

    return uploaded_form

async def content_extracter(uploaded_form, prompt):
    unformatted_extracted_content = await client.aio.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_uri(
                file_uri=uploaded_form.uri,
                mime_type='application/pdf'
            ),
            prompt
        ],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        )
    )

    return unformatted_extracted_content

def get_prompt(form_type):
    prompt_func = getattr(prompts, form_type, None)
    if prompt_func is None:
        raise ValueError(f"No prompt function found for form type: {form_type}")
    prompt_text = prompt_func()
    return prompt_text