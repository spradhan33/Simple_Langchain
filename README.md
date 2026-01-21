# 🍽️ Simple LangChain Restaurant Name & Menu Generator

A beginner-friendly **Streamlit + LangChain** project that generates a **unique restaurant name** and a **list of popular dishes** based on the selected cuisine using an AI language model.

## 📖 Project Overview

This project is a simple AI-powered web application built using **Streamlit** and **LangChain**.  
It allows users to select a cuisine type and instantly generates:

- A **unique and fancy restaurant name**
- A **list of popular dishes** related to that cuisine

The main goal of this project is to understand how **LangChain prompt templates**, **LLM chaining**, and **Streamlit UI** work together in a real-world application.  
It is designed to be **beginner-friendly**, modular, and easy to extend with different language models such as **Google Gemini** or **local models using Ollama**.


## 🚀 Features

- Dropdown menu to select cuisine type
- Generates:
  - One fancy and unique restaurant name
  - Five popular dishes for the selected cuisine
- Clean and simple Streamlit user interface
- Uses LangChain prompt chaining
- Easy to understand and beginner-friendly code

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – for building the web interface
- **LangChain** – for prompt templates and chaining
- **Google Gemini** – language model
- **python-dotenv** – for managing environment variables

```bash
## 📂 Project Structure

Langchain_P1/
│
├── app.py # Streamlit frontend
├── langchain_helper.py # LangChain logic (LLM + prompts)
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files and folders
├── .env # API keys (not pushed to GitHub)
├── venv/ # Virtual environment (not pushed)
└── pycache/ # Python cache files
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/spradhan33/Simple_Langchain.git
cd Simple_Langchain
```
```bash
2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate
```
```bash
3️⃣ Install dependencies
pip install -r requirements.txt
```
```bash
4️⃣ Set up environment variables
Create a .env file in the project root directory and add:
GOOGLE_API_KEY=your_api_key_here
⚠️ Do not push the .env file to GitHub.
```

## ▶️ Run the Application

After completing the setup, start the Streamlit app using:

```bash
streamlit run app.py
http://localhost:8501
```

📌 **Why this section matters**
- Makes it crystal clear **how to start the app**
- Prevents confusion for reviewers and users

## 🧪 Example Output

**Cuisine Selected:** Indian  

**Restaurant Name:**  
Royal Spice Palace  

**Menu Items:**
- Butter Chicken  
- Paneer Tikka  
- Dal Makhani  
- Biryani  
- Masala Dosa  






