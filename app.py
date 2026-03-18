from fastapi import FastAPI, Request, Form, Body, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

with open("students_dataset.json") as f:
    students = json.load(f)

faculty_accounts = {
    "faculty": "faculty123"
}

def find_student(reg_no):
    for s in students:
        if s["univ_reg_no"] == reg_no:
            return s
    return None


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("student_login.html", {"request": request})


# STUDENT LOGIN
@app.post("/student-login", response_class=HTMLResponse)
def student_login(request: Request, reg_no: str = Form(...), password: str = Form(...)):

    student = find_student(reg_no)

    if student and password == "student123":
        return templates.TemplateResponse(
            "student_dashboard.html",
            {"request": request, "student": student}
        )

    return HTMLResponse("Invalid Login")


# FACULTY LOGIN
@app.get("/faculty", response_class=HTMLResponse)
def faculty_page(request: Request):
    return templates.TemplateResponse("faculty_login.html", {"request": request})


@app.post("/faculty-login", response_class=HTMLResponse)
def faculty_login(request: Request, username: str = Form(...), password: str = Form(...)):

    if username in faculty_accounts and faculty_accounts[username] == password:
        return templates.TemplateResponse(
            "faculty_dashboard.html",
            {"request": request, "students": students}
        )

    return HTMLResponse("Invalid Faculty Login")


@app.post("/faculty-login-json")
def api_faculty_login(payload: dict = Body(...)):
    username = payload.get("username")
    password = payload.get("password")

    if not username or not password:
        raise HTTPException(status_code=400, detail="username and password are required")

    if username in faculty_accounts and faculty_accounts[username] == password:
        return JSONResponse({"status": "ok", "role": "faculty"})

    raise HTTPException(status_code=401, detail="Invalid Faculty Login")


# API endpoints for Streamlit frontend
@app.post("/login-etlab")
def api_login_etlab(payload: dict = Body(...)):
    reg_no = payload.get("reg_no")
    password = payload.get("password")

    if not reg_no or not password:
        raise HTTPException(status_code=400, detail="reg_no and password are required")

    student = find_student(reg_no)
    if not student or password != "student123":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return JSONResponse({"status": "ok", "student": student})


@app.post("/student-chat")
def api_student_chat(payload: dict = Body(...)):
    reg_no = payload.get("reg_no")
    message = (payload.get("message") or "").lower()

    student = find_student(reg_no)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Simple keyword-based replies
    if "cgpa" in message:
        return {"response": f"CGPA: {student.get('cgpa')}"}

    if "skill" in message:
        skills = student.get("skills", [])
        return {"response": "Skills:\n" + "\n".join(skills) if skills else "No skills found."}

    if "certificate" in message or "cert" in message:
        certs = student.get("uploaded_certificates", {})
        lines = []
        for cat, items in certs.items():
            if items:
                lines.append(f"{cat.capitalize()}: {len(items)}")
        return {"response": "Certificates:\n" + "\n".join(lines) if lines else "No certificates uploaded."}

    return {"response": "Sorry, I can only answer questions about CGPA, skills, and certificates right now."}


@app.post("/faculty-chat")
def api_faculty_chat(payload: dict = Body(...)):
    query = (payload.get("query") or "").lower().strip()

    # Exact student lookup (by reg no / name)
    for s in students:
        if s["univ_reg_no"].lower() in query or s["name"].lower() in query:
            certs = s.get("uploaded_certificates", {})
            hackathons = [c.get("event", "") for c in certs.get("hackathons", [])]
            return {
                "response": (
                    f"Student: {s['name']}\n"
                    f"KTU ID: {s['univ_reg_no']}\n"
                    f"CGPA: {s['cgpa']}\n"
                    f"Skills: {', '.join(s.get('skills', []))}\n"
                    f"Certificates: {', '.join(hackathons) if hackathons else 'None'}\n"
                )
            }

    # Parse CGPA threshold and required skills
    import re

    threshold = None
    if "cgpa" in query:
        m = re.search(r"(>=|<=|>|<|=)?\s*(\d+\.?\d*)", query)
        if m:
            threshold = float(m.group(2))

    # Detect requested skills from query using known skills in dataset
    known_skills = {skill.lower() for s in students for skill in s.get("skills", [])}
    requested_skills = [w for w in re.findall(r"\b\w+\b", query) if w in known_skills]

    # Strict filter (all conditions must match)
    def matches(student: dict):
        if threshold is not None and student.get("cgpa", 0) < threshold:
            return False
        for skill in requested_skills:
            if skill not in [s.lower() for s in student.get("skills", [])]:
                return False
        return True

    strict_matches = [s for s in students if matches(s)]

    best_match_mode = any(k in query for k in ["suggest", "recommend", "best match", "top match"])

    if strict_matches:
        sorted_matches = sorted(strict_matches, key=lambda x: x.get("cgpa", 0), reverse=True)
        rows = [f"{s['name']} ({s['univ_reg_no']}) - CGPA {s['cgpa']} - Skills: {', '.join(s.get('skills', []))}" for s in sorted_matches[:5]]
        return {"response": "Matching students:\n" + "\n".join(rows)}

    if best_match_mode:
        # Fall back to best-scoring students (cgpa + skill overlap)
        def score(student: dict):
            cgpa_score = student.get("cgpa", 0)
            skill_score = len(set([s.lower() for s in student.get("skills", [])]) & set(requested_skills))
            return cgpa_score * 2 + skill_score

        best = sorted(students, key=score, reverse=True)[:5]
        rows = [f"{s['name']} ({s['univ_reg_no']}) - CGPA {s['cgpa']} - Skills: {', '.join(s.get('skills', []))}" for s in best]
        return {"response": "Suggested students (best match):\n" + "\n".join(rows)}

    # Return guided help if nothing found
    if threshold is not None or requested_skills:
        parts = []
        if threshold is not None:
            parts.append(f"CGPA >= {threshold}")
        if requested_skills:
            parts.append("skills: " + ", ".join(requested_skills))
        return {"response": f"No students found matching ({'; '.join(parts)}). Try adjusting your query or ask for a suggestion."}

    return {"response": "No student found matching that query. Try asking about a student name/ID, CGPA, or skills."}


@app.post("/upload-certificate")
def upload_certificate(payload: dict = Body(...)):
    # This is a stub endpoint; a real implementation would store the uploaded file info.
    return {"status": "ok", "message": "Certificate upload simulated."}
