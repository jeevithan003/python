person = {
    "name": "Alice",
    "age": 28,
    "gender": "Female",
    "city": "San Francisco",
    "email": "alice@example.com",
    "phone": "555-1234",
    "interests": ["reading", "traveling", "photography"],
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science",
        "school": "University of California"
    },
    "work_experience": [
        {
            "position": "Software Engineer",
            "company": "Tech Corp",
            "years": 3
        },
        {
            "position": "Web Developer",
            "company": "WebSolutions",
            "years": 2
        }
    ]
}


for k,v in person.items():
    print(f"{k}, {v}", end=" ")
