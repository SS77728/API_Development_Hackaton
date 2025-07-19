from fastapi import FastAPI, HTTPException
from typing import List, Optional
from data import courses, faculty
from models import Course, Faculty
from collections import Counter

app = FastAPI(title="College API", description="API to get course & faculty info")


@app.get("/")
def read_root():
    return {"message": "Welcome to the College API!"}


@app.get("/courses", response_model=List[Course])
def get_courses(
    department: Optional[str] = None,
    credits: Optional[int] = None,
    search: Optional[str] = None
):
    result = courses
    if department:
        result = [c for c in result if c["department"].lower() == department.lower()]
    if credits:
        result = [c for c in result if c["credits"] == credits]
    if search:
        result = [c for c in result if search.lower() in c["name"].lower()]

    if not result:
        raise HTTPException(status_code=404, detail="No courses found with the given filters")
    return result


@app.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int):
    for c in courses:
        if c["id"] == course_id:
            return c
    raise HTTPException(status_code=404, detail="Course not found")


@app.get("/faculty", response_model=List[Faculty])
def get_faculty(
    department: Optional[str] = None,
    specialization: Optional[str] = None
):
    result = faculty
    if department:
        result = [f for f in result if f["department"].lower() == department.lower()]
    if specialization:
        result = [f for f in result if any(specialization.lower() in s.lower() for s in f["specialization"])]

    if not result:
        raise HTTPException(status_code=404, detail="No faculty found with the given filters")
    return result


@app.get("/faculty/{faculty_id}", response_model=Faculty)
def get_faculty_member(faculty_id: int):
    for f in faculty:
        if f["id"] == faculty_id:
            return f
    raise HTTPException(status_code=404, detail="Faculty member not found")


@app.get("/faculty/{faculty_id}/courses", response_model=List[Course])
def get_courses_by_faculty(faculty_id: int):
    crf = [c for c in courses if c["faculty_id"] == faculty_id]
    if not crf:
        raise HTTPException(status_code=404, detail="No courses found for this faculty member")
    return crf


@app.get("/stats/courses")
def course_stats():
    total = len(courses)
    by_department = Counter(c["department"] for c in courses)
    return {
        "total_courses": total,
        "courses_by_department": dict(by_department)
    }


@app.get("/stats/faculty")
def faculty_stats():
    total = len(faculty)
    by_department = Counter(f["department"] for f in faculty)
    return {
        "total_faculty": total,
        "faculty_by_department": dict(by_department)
    }