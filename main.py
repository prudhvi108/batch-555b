from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student Details Management API")

# 1. In-Memory Database
students_db = {
    1: {"name": "Aarav", "age": 21, "course": "Data Science"},
    2: {"name": "Priya", "age": 22, "course": "Web Development"},
    3: {"name": "Rohan", "age": 20, "course": "AI & ML"},
}


# 2. Data Validation Model
class Student(BaseModel):
    name: str
    age: int
    course: str


# ==========================================
# 1. READ (GET) - View All or Filter by Course
# ==========================================


@app.get("/students/")
def get_students(course: str = None):
    if course:
        filtered = {
            s_id: s
            for s_id, s in students_db.items()
            if s["course"].lower() == course.lower()
        }
        return filtered

    return students_db
    
