# 📚 College RESTful API

A simple RESTful API built in Python to retrieve course and faculty data.  
Built as part of the **API_Development_Hackathon**.

---

## ✨ Features

- Retrieve all courses or filter by department, credits, or search term
- Retrieve a specific course by ID
- Retrieve all faculty or filter by department or specialization
- Retrieve a specific faculty member by ID
- Get all courses taught by a faculty member
- View basic statistics about courses and faculty
- Test easily with Postman

---

## 🛠 Installation

```bash
git clone https://github.com/SS77728/API_Development_Hackaton.git
cd API_Development_Hackaton
pip install fastapi uvicorn
'''

▶️ **Running the API**

```bash
uvicorn main:app --reload
'''

By default, the API will be available at:

- 🌐 **Root:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- 📑 **Docs (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 How to Test with Postman

### ✅ Get all courses

- **Method:** `GET`  
- **URL:** `http://127.0.0.1:8000/courses`

**Example Response:**
```json
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


