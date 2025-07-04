# 🔥 Streamlit + LangChain + Cohere Cold Email Generator (Python Version)
# ✅ Web UI to upload resume and input job description

# 📄 Save this file as `app.py`

import streamlit as st
import os
from langchain_community.embeddings import CohereEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

# API Key from .env
cohere_api_key = os.getenv("COHERE_API_KEY")

# Workaround for Cohere bug: pass user_agent manually
cohere_config = {
    "cohere_api_key": cohere_api_key,
    "user_agent": "langchain"
}

# Initialize LLM and embeddings with explicit models
llm = Cohere(model="command-r-plus", **cohere_config)
embeddings = CohereEmbeddings(model="embed-english-v3.0", **cohere_config)

st.title("Cold Email Generator")
st.markdown("Generate an job email tailored for you.")

resume_file = st.file_uploader("Upload your resume (Markdown or TXT)", type=["md", "txt"])
job_description = st.text_area("Paste the job description")

if st.button("Generate Cold Email"):
    if resume_file and job_description:
        resume_text = resume_file.read().decode("utf-8")

        # Embed resume
        documents = [{"page_content": resume_text}]
        vectorstore = FAISS.from_texts([doc["page_content"] for doc in documents], embeddings)
        results = vectorstore.similarity_search(job_description, k=1)
        relevant_resume = results[0].page_content if results else resume_text

        # Prompt template
        prompt = PromptTemplate.from_template('''
You are an expert assistant writing professional cold emails for job applications.
Based on this resume:

{resume}

Write a short, impactful, personalized cold email for this job:

{job}

Email:
''')

        chain = LLMChain(llm=llm, prompt=prompt)

        try:
            response = chain.run({"resume": relevant_resume, "job": job_description})
            st.subheader("Your email, specifically tailored according to your resume.")
            st.write(response or "⚠️ Empty response. Check the inputs or Cohere settings.")
        except Exception as e:
            st.error(f"❌ Error generating email: {e}")
    else:
        st.warning("Please upload your resume and enter a job description.")
