# College RESTful API

A simple RESTful API built in Python to serve course and faculty data.  
Built as part of the **API_Development_Hackathon**.

## 📦 Features
- Retrieve all courses or filter by department, credits, or search term
- Retrieve a specific course by ID
- Retrieve all faculty or filter by department or specialization
- Retrieve a specific faculty member by ID
- Get all courses taught by a faculty member
- View basic statistics about courses and faculty
- Ready to test via Postman

---

## 🛠 Installation

```bash
git clone https://github.com/SS77728/API_Development_Hackaton.git
cd API_Development_Hackaton
pip install fastapi uvicorn

▶️ How to Run

Start the API locally:

uvicorn main:app --reload

The API will run at:

    http://127.0.0.1:8000/

You can explore interactive API docs at:

    http://127.0.0.1:8000/docs

🧪 How to Test with Postman
1. Get all courses

    Method: GET

    URL: http://127.0.0.1:8000/courses

Example Response:

[
  {
    "id": 1,
    "name": "Introduction to AI",
    "code": "AI101",
    "description": "Learn the basics of artificial intelligence, including machine learning and neural networks.",
    "credits": 3,
    "department": "Computer Science",
    "prerequisites": [],
    "faculty_id": 1
  },
  {
    "id": 2,
    "name": "Robotics Intelligence",
    "code": "ROBO201",
    "description": "Explore the principles of robotics and how AI is applied in robotic systems.",
    "credits": 4,
    "department": "Mechanical Engineering",
    "prerequisites": ["AI101"],
    "faculty_id": 2
  }
]

2. Get a single course by ID

    Method: GET

    URL: http://127.0.0.1:8000/courses/1

3. Filter courses

    Method: GET

    URL: http://127.0.0.1:8000/courses?department=Computer Science

    You can also filter by:

        credits → e.g. /courses?credits=3

        search → e.g. /courses?search=AI

4. Get all faculty

    Method: GET

    URL: http://127.0.0.1:8000/faculty

5. Get a faculty member by ID

    Method: GET

    URL: http://127.0.0.1:8000/faculty/1

6. Filter faculty

    Method: GET

    URL: http://127.0.0.1:8000/faculty?department=Computer Science

    Or by specialization:

        /faculty?specialization=AI

7. Get all courses taught by a faculty member

    Method: GET

    URL: http://127.0.0.1:8000/faculty/1/courses

8. View statistics

    Courses stats: GET → /stats/courses

    Faculty stats: GET → /stats/faculty

🏗 Project Structure

API_Development_Hackaton/
├── data.py       # Course & faculty data
├── main.py       # API endpoints
├── models.py     # Pydantic models
├── LICENSE       # Project license
└── README.md     # Project info
