import streamlit as st
from dotenv import load_dotenv
import io
import os
import PyPDF2
import google.generativeai as genai
load_dotenv()

st.title("")
st.divider()
st.badge("PREDICTION")
st.markdown("UPLOAD YOUR RESUME AND AI POWERED ROASTING")

st.file_uploader("upload your resume here([PDF and TXT only)",type=["PDF","TXT"])
job_role = st.text_input("ENTER THE JOB ROLE THAT YOU ARE TARGETING")
analyze = st.button("Analyze resume")
print(analyze)

def extract_text_form_pdf(file_bytes):
    reader = PyPDF2.PdfReader(file_bytes)
    return"\n".join(page.extract_text()or""for page in reader.pager)
if analyze and uploaded_file: # pyright: ignore[reportUndefinedVariable]
 pass
def extract_text(uploaded_file):
    """Extracts text form an uploaded pdf of txt"""
    file_type = uploaded_file.type
    with io.BytesIO(uploaded_file.read()) as file_bytes:
        return extract_text_form_pdf(file_bytes)
    if file_type == "aplication/pdf":
        pass
    elif file_type == "text/plain":
         return uploaded_file.read().decode("utf.8-")
    
if analyze and uploaded_file: # type: ignore
    try:
        file_content = extract_text(uploaded_file) # pyright: ignore[reportUndefinedVariable]
      
      
        if not file_content.strip():
             st.error("file does not have any content")
             st.stop()
                   
             prompt = """
you are brufully honest,non-sense HR expert who,s been reviewing resumes for recsdes.
roast this resume like you are a comedy stage but still give same usefull insights feekback.
don,t hold back-be
sarcastic, wiffy and critical where needed,
would make this resume actully land a job in
{job_role}for a good company
here is the resume.go wild:
{file_content}
make it sting and make sure to keep in 150 words"""
             model = genai.GenerativeModel("model/gemini-1.5 flash")
             response = model.generate_content(prompt)
             st.markdown("## Analysis results")
             st.markdown(response.text)
    except Exception as e:
         st.error(f"An error accured")
