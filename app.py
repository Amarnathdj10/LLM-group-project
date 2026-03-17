from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
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