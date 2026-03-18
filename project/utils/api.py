import json
from typing import Optional

import requests

BASE_URL = "http://localhost:8000"


def _post(path: str, payload: dict):
    url = f"{BASE_URL}{path}"
    try:
        r = requests.post(url, json=payload, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def login_etlab(reg_no: str, password: str) -> dict:
    return _post("/login-etlab", {"reg_no": reg_no, "password": password})


def faculty_login(username: str, password: str) -> dict:
    return _post("/faculty-login-json", {"username": username, "password": password})


def student_chat(reg_no: str, message: str) -> dict:
    return _post("/student-chat", {"reg_no": reg_no, "message": message})


def faculty_chat(query: str) -> dict:
    return _post("/faculty-chat", {"query": query})


def upload_certificate(reg_no: str, category: str, title: str, timestamp: str) -> dict:
    return _post(
        "/upload-certificate",
        {
            "reg_no": reg_no,
            "category": category,
            "title": title,
            "timestamp": timestamp,
        },
    )


def load_local_students(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
