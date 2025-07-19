courses = [
    {
        "id": 1,
        "name": "Introduction to AI",
        "code": "AI101",
        "description": "Learn the basics of artificial intelligence, including machine learning and neural networks.",
        "credits": 3,
        "department": "Computer Science",
        "prerequisites": [],
        "faculty_id": 1,
    },
    {
        "id": 2,
        "name": "Robotics Intelligence",
        "code": "ROBO201",
        "description": "Explore the principles of robotics and how AI is applied in robotic systems.",
        "credits": 4,
        "department": "Mechanical Engineering",
        "prerequisites": ["AI101"],
        "faculty_id": 2,
    }
]

faculty = [
    {
        "id": 1,
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice@iiitdm.ac.in",
        "department": "Computer Science",
        "specialization": ["AI", "Machine Learning"],
        "office": "Room 101",
        "office_hours": "Mon-Fri 10:00-12:00",
    },
    {
        "id": 2,
        "first_name": "Tom",
        "last_name": "Cruise",
        "email": "tomcruise@iiitdm.ac.in",
        "department": "Mechanical Engineering",
        "specialization": ["Robotics", "Control Systems"],
        "office": "Room 202",
        "office_hours": "Mon-Fri 14:00-16:00",
    }
]