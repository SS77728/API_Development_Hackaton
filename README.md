📚 College RESTful API

A simple RESTful API built in Python to serve course and faculty data.
Built as part of the API_Development_Hackathon.



✨ Features





Retrieve all courses or filter by department, credits, or search term



Retrieve a specific course by ID



Retrieve all faculty or filter by department or specialization



Retrieve a specific faculty member by ID



Get all courses taught by a faculty member



View basic statistics about courses and faculty



Test easily with Postman



🛠 Installation





Clone the repository:

git clone https://github.com/SS77728/API_Development_Hackaton.git
cd API_Development_Hackaton



Install dependencies:

pip install fastapi uvicorn



Run the API:

uvicorn main:app --reload

By default, the API will be available at:





Root: http://127.0.0.1:8000/



Docs (Swagger UI): http://127.0.0.1:8000/docs



🧪 How to Test with Postman

✅ Get All Courses





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

🔍 Filter Courses





By department:

GET http://127.0.0.1:8000/courses?department=Computer Science



By credits:

GET http://127.0.0.1:8000/courses?credits=3



By search term:

GET http://127.0.0.1:8000/courses?search=AI

📌 Get Single Course by ID





Method: GET



URL: http://127.0.0.1:8000/courses/1

👨‍🏫 Get All Faculty





Method: GET



URL: http://127.0.0.1:8000/faculty

🔍 Filter Faculty





By department:

GET http://127.0.0.1:8000/faculty?department=Computer Science



By specialization:

GET http://127.0.0.1:8000/faculty?specialization=AI

👨‍🏫 Get Single Faculty by ID





Method: GET



URL: http://127.0.0.1:8000/faculty/1

📚 Get Courses Taught by a Faculty Member





Method: GET



URL: http://127.0.0.1:8000/faculty/1/courses

📊 Statistics





Total courses & by department:

GET http://127.0.0.1:8000/stats/courses



Total faculty & by department:

GET http://127.0.0.1:8000/stats/faculty



🏗 Project Structure

API_Development_Hackaton/
├── data.py       # Contains sample data
├── main.py       # API endpoints
├── models.py     # Pydantic models
├── LICENSE       # License info
└── README.md     # This file



🖼 Screenshots

Place your screenshots inside an images/ folder, then reference them here:







Running API



Swagger UI



Postman Test





[Insert Image]



[Insert Image]



[Insert Image]



📄 License

This project is licensed under the MIT License.
See the LICENSE file for details.
