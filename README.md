# LLM-group-project

This project is a **FastAPI-based student/faculty portal** with a simple templated front-end and built-in dataset support. It also contains model artifacts and training scripts (for an LLM-related task), but the web app is the primary runnable component.

## ✅ What this project provides

- **Web UI (FastAPI + Jinja2 templates)**
  - Student login + dashboard
  - Faculty login + dashboard
- **Static assets** in `static/` (CSS)
- **Student dataset** in `students_dataset.json`
- **Model/training artifacts** in `college_model/` (adapter model, tokenizer, checkpoint, etc.)

## 🚀 Run the web app (FastAPI)

1) Open a terminal and go to the project directory:

```powershell
cd C:\Users\VICTUS\Desktop\llm\LLM-group-project
```

2) Install dependencies:

```powershell
pip install fastapi uvicorn python-multipart
```

3) Run the server:

```powershell
uvicorn app:app --reload
```

4) Open the web UI in your browser:

- Student login: http://127.0.0.1:8000/
- Faculty login: http://127.0.0.1:8000/faculty

---

## 🚀 Run the Streamlit UI (Modern Portal)

This repository also includes a Streamlit-based front-end that behaves like a modern academic ERP portal.

1) Change into the Streamlit project folder:

```powershell
cd C:\Users\VICTUS\Desktop\llm\LLM-group-project\project
```

2) Install Streamlit and support packages:

```powershell
pip install streamlit streamlit-option-menu pandas plotly requests
```

3) Start the FastAPI backend in a separate terminal (needed for full AI/chat and login functionality):

```powershell
cd C:\Users\VICTUS\Desktop\llm\LLM-group-project
uvicorn app:app --reload
```

4) Start the Streamlit app:

```powershell
cd C:\Users\VICTUS\Desktop\llm\LLM-group-project\project
streamlit run app.py
```

5) Open the Streamlit UI in your browser (the URL is shown in the terminal).

---

## 🗂 Key files/folders

- `app.py` – FastAPI server and routes
- `templates/` – HTML templates (Jinja2)
- `static/` – CSS and other static assets
- `students_dataset.json` – student data displayed in dashboards
- `college_model/` – LLM model artifacts and training checkpoints

## 🛠 Notes / Common issues

- If you see `Form data requires "python-multipart"`, install it:
  ```powershell
  pip install python-multipart
  ```

- Make sure you run `uvicorn` from the folder where `app.py` lives.

---

## 🧠 Optional enhancements (ideas)

- Add authentication/session support (instead of a fixed password)
- Add API endpoints and use JavaScript for a richer UI (SPA-style)
- Add forms to modify/save student data
- Add unit tests for routes and HTML responses
