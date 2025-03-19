import os
import google.generativeai as genai
import pandas as pd

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df.dropna(inplace=True)
    return df