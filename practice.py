from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI(title="CRUD API")


# Pydantic model
class Student(BaseModel):
    name: str
    age: int
    course: str


# Temporary database
students = []
next_id = 1


# =========================================================
# CREATE - POST /students
# =========================================================

@app.post("/students")
def create_students(student: Student):
    global next_id

    new_student = {
        "id": next_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(new_student)

    next_id += 1

    return {
        "message": "Student created successfully!",
        "student": new_student
    }


# =========================================================
# READ ALL - GET /students
# =========================================================

@app.get("/students")
def get_students():
    return students


# =========================================================
# READ ONE - GET /students/{student_id}
# =========================================================

@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:

        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# =========================================================
# UPDATE - PUT /students/{student_id}
# =========================================================

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for student in students:

        if student["id"] == student_id:

            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course

            return {
                "message": "Student updated successfully!",
                "student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# =========================================================
# DELETE - DELETE /students/{student_id}
# =========================================================

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student["id"] == student_id:

            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully!",
                "student": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )