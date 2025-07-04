# Cold Email Generator

A basic Cold Email Generator built using Streamlit, Langchain framework and Cohere's command-r-plus model.

# Features

->Allows the user to input their resume

->Allows the user to input the job description

->Generates an email based on the description and the user resume

# How to use
![image](https://github.com/user-attachments/assets/64f5dab7-0b75-4b2a-b859-b32332b4bdae)

1. Upload the resume in .txt or .md format
   ![image](https://github.com/user-attachments/assets/60a750d6-0034-4300-be5d-42202d2c5ed0)

2. Give the job description and click on "Generate Cold Email"
   ![image](https://github.com/user-attachments/assets/dee10454-ac69-45d5-a6ca-3059699e0d4d)

3. The email will be displayed in a few seconds
 ![image](https://github.com/user-attachments/assets/1f4e7b5a-3758-4354-bc11-090cbc519da6)

# Installation
1. Clone the repository

   git clone https://github.com/yourusername/cold-email-generator.git
   
   cd cold-email-generator

2. Create and activate a virtual environment
   
   python -m venv venv
   
   .\venv\Scripts\Activate.ps1     

3. Install dependencies

   pip install -r requirements.txt

4. Create a .env file in the root directory and add your Cohere API key:
   
   COHERE_API_KEY=your-cohere-api-key-here

5. Run the app
   
   streamlit run app.py
   
   Then open http://localhost:8501 in your browser.
