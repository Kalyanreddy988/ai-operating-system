# 🤖 AI Operating System (AI-OS)

An end-to-end **AutoML-powered AI Operating System** that allows users to upload datasets, automatically train machine learning models, evaluate performance, explain results, and download trained models — all through a clean web interface.

---

## 🚀 Features

- 📁 Upload CSV datasets
- 🧠 Automatic problem detection (Regression / Classification)
- ⚙️ AutoML model selection
- 📊 Performance metrics (Accuracy / R² Score)
- 🧩 LLM-based explanation of results
- 💾 Download trained ML models (`.joblib`)
- 🎨 Modern, responsive UI (React + Vite)
- 🔌 Modular backend architecture (FastAPI)

---

## 🧠 Supported Machine Learning Tasks

### ✅ Supervised Learning (Implemented)

#### Regression
- Linear Regression
- Random Forest Regressor

#### Classification
- Logistic Regression
- Random Forest Classifier

> ⚠️ Note: Unsupervised learning (clustering, PCA, anomaly detection) is **planned** but not implemented yet.

---

## 🏗️ System Architecture
Frontend (React + Vite)
        |
        |  HTTP (REST API)
        v
Backend (FastAPI)
        |
        ├── Data Loader
        ├── AutoML Engine
        ├── Model Trainer
        ├── Evaluator
        ├── LLM Explanation Generator
        └── Model Storage & Download


---

## 📂 Project Structure

ai_os/
├── app/
│   ├── main.py
│   ├── controller.py
│   ├── agents/
│   │   ├── executor.py
│   │   ├── planner.py
│   │   └── memory.py
│   ├── tools/
│   │   ├── datatools.py
│   │   ├── mltools.py
│   │   └── model_selector.py
│   └── core/
│       ├── llm_client.py
│       └── config.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── TaskForm.jsx
│   │   │   ├── FileUpload.jsx
│   │   │   └── AIBackground.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── saved_models/
├── uploads/
├── requirements.txt
├── README.md
└── .gitignore


---

## 🛠️ Tech Stack

### Backend
- Python 3.11
- FastAPI
- Scikit-learn
- Pandas, NumPy
- Joblib

### Frontend
- React
- Vite
- CSS (custom gradients & animations)

---

## ▶️ How to Run the Project

### 1️⃣ Backend Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend runs at:
http://127.0.0.1:8000

### 2️⃣ Frontend Setup
cd frontend
npm install
npm run dev

Frontend runs at:
http://localhost:5173


📥 Downloading Trained Models

After training:

-->Click “Download Trained Model”
-->A .joblib file is downloaded
-->Can be reused for inference in any Python environment

Example:
import joblib
model = joblib.load("model.joblib")


🧠 LLM Explanation

The system generates a human-readable explanation describing:
    -->Model behavior
    -->Performance quality
    -->Improvement suggestions

🔮 Future Enhancements (Planned):

🔍 Unsupervised Learning (KMeans, PCA, DBSCAN)
📈 Feature importance visualization
📊 Cross-validation dashboard
👤 User authentication
☁️ Cloud deployment
🤖 Agentic AI planning layer


🎓 Academic & Resume Value

Demonstrates end-to-end ML system design
Covers AutoML, backend APIs, frontend UI

Suitable for:
Final year project
Resume
Research extension
Startup prototype

👨‍💻 Author

Kalyan Reddy
AI / ML / Full-Stack Enthusiast