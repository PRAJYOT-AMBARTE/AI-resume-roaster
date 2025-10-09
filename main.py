# import streamlit as st
# from dotenv import load_dotenv
# import io
# import os
# import PyPDF2
# import google.generativeai as genai
# load_dotenv()

# st.title("")
# st.divider()
# st.badge("PREDICTION")
# st.markdown("UPLOAD YOUR RESUME AND AI POWERED ROASTING")

# st.file_uploader("upload your resume here([PDF and TXT only)",type=["PDF","TXT"])
# job_role = st.text_input("ENTER THE JOB ROLE THAT YOU ARE TARGETING")
# analyze = st.button("Analyze resume")
# print(analyze)

# def extract_text_form_pdf(file_bytes):
#     reader = PyPDF2.PdfReader(file_bytes)
#     return"\n".join(page.extract_text()or""for page in reader.pager)
# if analyze and uploaded_file: # pyright: ignore[reportUndefinedVariable]
#  pass
# def extract_text(uploaded_file):
#     """Extracts text form an uploaded pdf of txt"""
#     file_type = uploaded_file.type
#     with io.BytesIO(uploaded_file.read()) as file_bytes:
#         return extract_text_form_pdf(file_bytes)
#     if file_type == "aplication/pdf":
#         pass
#     elif file_type == "text/plain":
#          return uploaded_file.read().decode("utf.8-")
    
# if analyze and uploaded_file: # type: ignore
#     try:
#         file_content = extract_text(uploaded_file) # pyright: ignore[reportUndefinedVariable]
      
      
#         if not file_content.strip():
#              st.error("file does not have any content")
#              st.stop()
                   
#              prompt = """
# you are brufully honest,non-sense HR expert who,s been reviewing resumes for recsdes.
# roast this resume like you are a comedy stage but still give same usefull insights feekback.
# don,t hold back-be
# sarcastic, wiffy and critical where needed,
# would make this resume actully land a job in
# {job_role}for a good company
# here is the resume.go wild:
# {file_content}
# make it sting and make sure to keep in 150 words"""
#              model = genai.GenerativeModel("model/gemini-1.5 flash")
#              response = model.generate_content(prompt)
#              st.markdown("## Analysis results")
#              st.markdown(response.text)
#     except Exception as e:
#          st.error(f"An error accured")
import streamlit as st
from dotenv import load_dotenv
import io
import os
import PyPDF2
import google.generativeai as genai

# Load .env variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page config for minimal look
st.set_page_config(
    page_title="AI Resume Roaster",
    page_icon="🔥",
    layout="centered"
)

# Custom CSS for minimalistic design
st.markdown("""
    <style>
    /* Main container padding */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    
    /* Title styling */
    h1 {
        font-weight: 300;
        letter-spacing: -0.5px;
    }
    
    /* Remove default padding */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 45px;
        font-weight: 500;
        background-color: #FF4B4B;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #FF3333;
        border: none;
    }
    
    /* Input fields */
    .stTextInput>div>div>input {
        border-radius: 8px;
    }
    
    /* File uploader */
    .stFileUploader>div>div {
        border-radius: 8px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Spacing */
    .element-container {
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🔥 AI Resume Roaster")
st.markdown("Upload your resume and get brutally honest feedback")
st.markdown("")

# Main content in a clean layout
col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader(
        "Resume (PDF/TXT)", 
        type=["pdf", "txt"],
        label_visibility="collapsed",
        help="Upload your resume in PDF or TXT format"
    )

with col2:
    job_role = st.text_input(
        "Target Role",
        placeholder="e.g., Software Engineer",
        label_visibility="collapsed"
    )

st.markdown("")
analyze = st.button("🔥 Roast My Resume", use_container_width=True)

def extract_text_from_pdf(file_bytes):
    reader = PyPDF2.PdfReader(file_bytes)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def extract_text(uploaded_file):
    """Extract text from uploaded PDF or TXT."""
    file_type = uploaded_file.type
    if file_type == "application/pdf":
        with io.BytesIO(uploaded_file.read()) as file_bytes:
            return extract_text_from_pdf(file_bytes)
    elif file_type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    else:
        return ""

if analyze:
    if not uploaded_file:
        st.warning("⚠️ Please upload a resume first")
        st.stop()
    
    if not job_role:
        st.warning("⚠️ Please enter a target job role")
        st.stop()

    with st.spinner("🔥 Preparing the roast..."):
        try:
            file_content = extract_text(uploaded_file)
            if not file_content.strip():
                st.error("❌ Could not extract text from the file")
                st.stop()

            prompt = f"""
You are a brutally honest HR expert reviewing resumes.
Roast this resume like a stand-up comedian but give useful feedback.
Be sarcastic, funny, and honest. Keep it under 200 words.

Target Role: {job_role}

Resume Content:
{file_content}
"""

            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(prompt)

            st.markdown("---")
            st.markdown("### 💬 The Verdict")
            st.markdown(response.text)
            
            # Add some space at the bottom
            st.markdown("")
            st.markdown("")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666; font-size: 0.9rem;'>Made with Streamlit & Gemini AI</p>",
    unsafe_allow_html=True
)