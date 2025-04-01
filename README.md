# AI-Powered Career Counselling and  Career Recommendations 

## 📌 Overview

Many students struggle with career decisions due to a lack of personalized guidance on suitable job roles, required skills, and industry trends. Additionally, optimizing resumes to align with employer expectations is a challenge. This project aims to develop an **AI-powered career guidance and resume optimization system** to help students make informed career choices and improve their job application success rates.
![image alt](https://github.com/amansaroj9616/Ai-Powered-Career-Counselling-and-Career-Recommendation-/blob/46487416df88d9454cb4d5611fdbe6c49c082791/screenshots/homepage.png)

## 🚀 Features

### 1️⃣ Personalized Career Recommendations
- 📊 Analyze academic performance, interests, skills, and market trends.
- 🛤️ Suggest suitable career paths (e.g., Software Engineer, Data Scientist, Researcher, etc.).
- 🎓 Recommend relevant courses, certifications, and projects to enhance employability.
- 🌍 Ensure career path alignment with current industry trends.

### 2️⃣ AI Career Recommendation and Resume Screener and Optimizer
- 📄 Evaluate a student's resume based on job descriptions.
- ✍️ Suggest improvements in formatting, keywords, and content.
- 🎯 Generate tailored resume versions for different job applications.

---
![image alt](https://github.com/amansaroj9616/Ai-Powered-Career-Counselling-and-Career-Recommendation-/blob/46487416df88d9454cb4d5611fdbe6c49c082791/screenshots/populararticals.png)
![image alt](https://github.com/amansaroj9616/Ai-Powered-Career-Counselling-and-Career-Recommendation-/blob/46487416df88d9454cb4d5611fdbe6c49c082791/screenshots/moreArticals.png)
![image alt](https://github.com/amansaroj9616/Ai-Powered-Career-Counselling-and-Career-Recommendation-/blob/46487416df88d9454cb4d5611fdbe6c49c082791/screenshots/login.png)
![image alt](https://github.com/amansaroj9616/Ai-Powered-Career-Counselling-and-Career-Recommendation-/blob/46487416df88d9454cb4d5611fdbe6c49c082791/screenshots/signup.png)
![image alt](https://github.com/amansaroj9616/Ai-Powered-Career-Counselling-and-Career-Recommendation-/blob/46487416df88d9454cb4d5611fdbe6c49c082791/screenshots/Screenshot%202025-03-21%20032247.png)
![image alt](https://github.com/amansaroj9616/Ai-Powered-Career-Counselling-and-Career-Recommendation-/blob/46487416df88d9454cb4d5611fdbe6c49c082791/screenshots/Screenshot%202025-03-21%20032225.png)


## 🛠️ Tech Stack
- **Frontend**: React.js / Next.js
- **Backend**: Node.js / Express.js / FastAPI
- **Database**: PostgreSQL / MongoDB
- **Machine Learning**: Python (Scikit-Learn, TensorFlow, NLP)
- **Cloud & Deployment**: AWS / GCP / Docker

---

## 🎯 How It Works

1. **User Input**: Students provide details about their education, skills, interests, and job preferences.
2. **AI Analysis**: The system processes the input, analyzing career trends and job market demands.
3. **Recommendations**: Users receive personalized career guidance and project/course suggestions.
4. **Resume Optimization**: The AI assesses and enhances the user’s resume based on job descriptions.

---

## 📂 Project Structure

📦 ai-career-guidance ├── 📁 backend │ ├── 📄 app.py │ ├── 📄 recommendation.py │ ├── 📄 resume_optimizer.py │ ├── 📄 requirements.txt │ └── 📁 models ├── 📁 frontend │ ├── 📄 App.js │ ├── 📄 CareerRecommendations.js │ ├── 📄 ResumeOptimizer.js │ └── 📁 components ├── 📄 README.md ├── 📄 package.json └── 📄 .gitignore

---

## 🖥️ Backend Code (FastAPI + Machine Learning)

### 📌 Install Dependencies
```bash
pip install fastapi uvicorn pandas scikit-learn nltk openai
```

📌 Backend API (app.py)
```
from fastapi import FastAPI
from recommendation import get_career_recommendations
from resume_optimizer import optimize_resume

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AI-Powered Career Guidance API"}

@app.post("/career-recommendation/")
def career_recommendation(user_data: dict):
    return get_career_recommendations(user_data)

@app.post("/resume-optimization/")
def resume_optimization(resume_text: dict):
    return optimize_resume(resume_text["content"])
```

📌 Career Recommendation Logic (recommendation.py)
```
import random

def get_career_recommendations(user_data):
    skills = user_data.get("skills", [])
    interests = user_data.get("interests", [])
    
    career_paths = {
        "Software Engineer": ["Python", "Java", "C++", "Web Development"],
        "Data Scientist": ["Python", "Machine Learning", "Statistics"],
        "AI Researcher": ["Deep Learning", "Neural Networks", "NLP"],
        "Cybersecurity Analyst": ["Network Security", "Penetration Testing"]
    }

    matches = [career for career, required_skills in career_paths.items() if any(skill in skills for skill in required_skills)]
    
    return {"recommended_careers": matches if matches else ["General IT Career"]}
```
📌 Resume Optimization (resume_optimizer.py)
```
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def optimize_resume(resume_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert resume optimizer."},
            {"role": "user", "content": f"Optimize this resume for a software engineering job: {resume_text}"}
        ]
    )
    return response["choices"][0]["message"]["content"]
```
🎨 Frontend Code (React.js)
📌 Install Dependencies
```
npm install axios react-router-dom
```
📌 App Component (App.js)
```
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import CareerRecommendations from "./CareerRecommendations";
import ResumeOptimizer from "./ResumeOptimizer";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<CareerRecommendations />} />
        <Route path="/resume" element={<ResumeOptimizer />} />
      </Routes>
    </Router>
  );
}

export default App;
```
📌 Career Recommendation Component (CareerRecommendations.js)
```
import React, { useState } from "react";
import axios from "axios";

function CareerRecommendations() {
  const [userData, setUserData] = useState({ skills: "", interests: "" });
  const [recommendations, setRecommendations] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post("http://localhost:8000/career-recommendation/", userData);
    setRecommendations(response.data.recommended_careers);
  };

  return (
    <div>
      <h1>AI Career Recommendations</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Skills (comma-separated)" onChange={(e) => setUserData({ ...userData, skills: e.target.value.split(",") })} />
        <input type="text" placeholder="Interests (comma-separated)" onChange={(e) => setUserData({ ...userData, interests: e.target.value.split(",") })} />
        <button type="submit">Get Recommendations</button>
      </form>
      <h2>Suggested Career Paths:</h2>
      <ul>
        {recommendations.map((career, index) => (
          <li key={index}>{career}</li>
        ))}
      </ul>
    </div>
  );
}

export default CareerRecommendations;
```

🚀 Getting Started
🔹 Prerequisites
Install Node.js, Python, and FastAPI
```
git clone https://github.com/your-repo/ai-career-guidance.git
cd ai-career-guidance
```
Install dependen
```
npm install  # For frontend
pip install -r backend/requirements.txt  # For backend
```
Start the development server:
```
npm start  # Frontend
uvicorn backend.app:app --reload  # Backend
```
🤝 Contributing
Want to contribute? Feel free to fork this repo and submit a pull request!

📄 License
This project is licensed under the MIT License.

⭐ Star this repository if you find it useful!
```

This README file includes:
- **Detailed explanations**
- **Code snippets for backend (FastAPI + ML)**
- **Frontend implementation (React.js)**
- **Setup instructions**

Let me know if you need modifications! 🚀










